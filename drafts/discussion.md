# *Intent* Server/Service -- a Proposal

## Abstract

The ChRIS ecosystem is a standard back-end / front-end architecture. The back-end, called **C**hRIS **U**nderlying **B**ack-**E**nd -- CUBE)  was designed to provide services to a multitude of possible clients. In reality, only one client currently exists: the reference front-end which is the ChRIS-UI web-app that provides all experiences related to ChRIS.

CUBE can be thought of as a low-level server of "primitive" services that clients assemble into larger, more complex structures that provide value. As a result, CUBE has focused on prividing a rich and expressive "vocabulary" that provides extensive coverage of all its internal structure and behavior (add data, create "feeds", query services, orchestrate applications into compute chains, etc). What CUBE does not provide are assembles of this vocabulary -- this is the responsibility of consumers of the CUBE API. One can think of CUBE as providing *words* and *syntax* but not *stories*.

Given that the ChRIS UI is the main consumer of the CUBE API, it has been tasked with not only providing a visual User Interface to the services CUBE provides, but also to assemble these CUBE services into behaviors of utility to users -- these behaviors are often multi-step processes requiring lots of back-and-forth with the backend. For instance, one common intent or user need is to find a dataset of interset and apply an analysis. This assmeblage is not provided by CUBE which only supplies the building blocks.

This non-backend assmeblage has proven cumbersome and clients (like the UI) often conflate business and visualization logic, or alternatively different clients have to re-invent common wheels. This proposal discusses an architectural addition, essentially an intermediate server that provides this assemblage for clients. Technically this can involve an expansion of the existing CUBE, or be provided by a wholly separate service. Both will be discussed, but ultimately this proposal will argue for a wholly separate service.

## Introduction

CUBE was designed to provide services to a *multitude* of clients by exposing a set of "primitives". By not focusing on a single client need, it evolved in a more general server that could be used in a variety of needs and context. More technically, CUBE adopted a <tt>colletion+json</tt> dialect to express its REST servies. By focusing on largely stateless low level primitives, CUBE is well suited to expose these in a RESTful API. Note this document is not concerned with discussing the <tt>collection+json</tt> dialect or its utility; rather this document identifies an impedenace mismatch between how parts of the system connect and proposes a solution at this mismatch level.

Of course, many things a user wants to do can be described as single tasks that really consist of many (possibly *stateful*) steps. For example, an extremely common need is to anonymize DICOM data that often contains Protected Health Information (PHI). To perform this, the following steps are performed by CUBE:

- Find the data in CUBE
- Create a new "Feed" (a "feed" is a single computational workflow in CUBE that starts with a root data node and all operations on that data progress from that node) with the data as root node
- Find the anonymization application in CUBE
- Attach this application to the root node's data
- Orchestrate the application to run
- Monitor the process and inform the user when complete

From the perspective of the user, this is a single atomic need, or *intent* which could be completely conveyed in a single pseudo-code function call, e.g:

<pre>
dataSet_analyze("Patient1234", "anonymization")
</pre>

The fact that *implementing* this single *intent* is a multistep process is largely of no concern or interest to the consumer of this intent. Indeed, we can recongize for a system such as CUBE and in a given context such as medical image analysis, clients care about servicing *intents*: the *what* not the *how* and not be concerned with the detail of how CUBE services this.

Note that the "user" here is not necessarily a human but could easily be another piece of software. In fact, users are interested in implementing these *intents*

This document will discuss the current architecture from the perspective of this observation. Starting with an overiew of the current setup, the document will highlight this *intent* mismatch, and then propose the most logical solution:how to implement/extend with an intent API or server.

Two possibilities will be discussed: extending the current CUBE, or creating a new, separate intent service. We will argue that a separate service is a good choice, especially for future-proofing and also for allowing agentic interfaces to CUBE.


## Current architecture and unintended consequences

### CUBE's API world view -- and the missing middleware

Early development of ChRIS and CUBE was evolutionary -- the final "shape" of the system -- its behavior, services, features, etc all generally developed organically as the system was being built and used concurrently. Since the final real time behavior was not known *a priori*, the backend focussed on its internal world adopted a self-discoverable API paradigm called <tt>collection+json</tt>. This provided a predictable uniformity and pattern language to the API as it was being developed, buffering it from variable and shifting needs as the actual system grew. In this world view, resources are collections linked by predictable relationships. In many ways, CUBE's API is syntactically similar to a graph transversal language rather than a set of iodmatic endpoints.

The mapping of this API idiom is "internally consistent" not "externally focused". The backend consists of *resources* linked in semantic relationship. Critically, these resources expose the building blocks that CUBE collects, **not** typical procedural endpoints that describe behavior. It is not a *service broker*, rather it is a semantic fabric describing

* what exists (plugins, feeds, users)
* what was done (plugin instances)
* what can be done next (additional plugin instances)

This is a declarative composition, not a list of procedural services. Essentially this disconnected CUBE from clients that need to provide procedural services, and shifted **orchestration burden to clients**. Since an intermediate intent layer was never developed, clients had to continually re-invent basic interactions with CUBE; worse, the ChRIS UI conflated business and presentation logic.

While the original aspiration of CUBE was to not be skewed to a given client use and remain a general purpose service, the real consequence has been a complete stifling of client-side development (other than the ChRIS UI no real clients exits) and in the ChRIS UI itself a complete entanglement of intent and presentation.


A core usage pattern for many users of ChRIS (and the ChRIS UI) is to collect data from the main Hospital PACS and do some processing on that data. This "processing" can be as simple as "downloading", as intermediate as "anonymization", or as complex as perform a arbitrary directed acyclic graph (DAG) of computing steps. Regardless of detail, all can be similarly described as "processing on the gathered data".

Here, we consider that story, "A user wants to use PACS Q/R to find some sets of data on the PACS (**Sea**rch)", then wants, on the results, to **Ga**ther a sub selection, and finally wants to assign some **P**rcocessing to that sub-selection. For simplicity we consider two process cases: (1) *Convert to NIfTI*; and (2) *Download*.

More easily expressed as, "I want to download all the MPRAGE series from Patient12345 and process them offline as NIfTI". An implicit intent is, *"Do this as simply as possible"*. A key concept here is an *Intent* -- which is perhaps best described as a single canonical action of importance to an end User. So this story can contain two *Intents*:

1. Download all MPRAGE series from Patient12345
2. Analyze all MPRAGE series of Patient12345 with FreeSurfer.

## Architectural Holes: front end; back end; middle end?

A key consideration, perhaps *the* key consideration, is serving such *Intents*. leveraging a meaningful architectural approach to best support or supplement this. The ChRIS ecosystem consists of a backend called CUBE and clients that consume the REST API exposed by CUBE. The semantics of this API notwithstanding, it is fair to describe CUBE as offering a rich set of *primitives* that allow a client to compose powerful interactions. These primitives follow a convention called "<tt>collection+json</tt>" -- the purpose of this discussion is not to address the pros and cons of <tt>collection+json</tt>, but to accept this as a given reality.


````
                  ┌──────────────────────────────────────────────┐
                  │                    ChRIS UI                  │
                  └───────────┬───────────────────────┬──────────┘
                              │                       │
                              │                       │
                              │                       │
                              │                       │
                              │                       │
                              ▼                       ▼
          ┌───────────────────┴───────────────────────┴───────────────────┐
          │                  REST API (colllection+json)                  │
          ├───────────────────────────────────────────────────────────────┤
          │                                                               │
          │                                                               │
          │                               CUBE                            │
          │                                                               │
          │                                                               │
          └───────────────────────────────────────────────────────────────┘
````



A direct implication, however, is that CUBE does not currently offer "value-added" or library type features. A javascript helper library is provided as a transliteration of the REST API into language specific objects, and the ChRIS UI leverages this to provide the entire experience. It is important to note that this library does not provide higher integrative functionality and maps to the existing REST API in an almost one-to-one fashion. Essentially the library simply saves the client the burden of having to make raw http requests.


````
                  ┌──────────────────────────────────────────────┐
                  │                    ChRIS UI                  │
                  ├──────────────────────────────────────────────┤
                  │           (javascript helper lib)            │
                  └───────────┬───────────────────────┬──────────┘
                              │                       │
                              │                       │
                              │                       │
                              │                       │
                              │                       │
                              ▼                       ▼
          ┌───────────────────┴───────────────────────┴───────────────────┐
          │                  REST API (colllection+json)                  │
          ├───────────────────────────────────────────────────────────────┤
          │                                                               │
          │                                                               │
          │                               CUBE                            │
          │                                                               │
          │                                                               │
          └───────────────────────────────────────────────────────────────┘
````

The "problem" is that value is provided by serving an *Intent*

For instance, a singular *Intent* such as "apply a FreeSurfer analysis to the MPRAGE data of Patent 12345" requires a complex orchestration of CUBE API calls and stateful processing. In fact, this "business logic" can be expressed as a stateful intent.

While a javascript and python librares exist as convenience, these libraries map the primitives of the CUBE API closely -- in other words they reflect the <tt>collection+json</tt> underpinning and provide library-based conveniences to call and process the REST API in an almost one-to-one fashion. Thus, the semantics of any given stateful *Intent* needs to be coded and managed by the client.

In this way, it is reasonable to observe that the *functional* distance between a simple client need and the backend is large. Moreover, this large distance runs the risk of duplication of client-side efforts for simple needs, depending on client programming language. Should a developer code a higher level helper library for example in javascript, then only javascript clients can use that library.

There are two obvious shallow solutions to this problem, and a more subtle one.

### Obvious shallow solution #1: Keep the status quo

First the obvious solution -- do nothing, or alternatively, continue as is. This is the so-called *null* solution and only presented really here for completeness. This solution shifts the burden completely on the client (as has been the development pattern until now). In reality we have enough data to suggest that client development has now slowed to a crawl due to technical debt, inertia, small development team, and conflation in the main client (i.e. the ChRIS UI) of business logic with presentation logic. Having the burden of business logic fall purely on the client does not seem feasible going forward.

Part of the problem is that, as stated earlier, the CUBE API is designed to provide a primitive RESTful (and non-stateful) view/interface. Nonetheless, pushing business logic to CUBE seems obvious shallow solution #2:

### Obvious shallow solution #2: Push business logic to CUBE

A client such as the ChRIS UI should focus on what it does best -- render a visual presentation of the ChRIS Universe, and not necessarily also provide all the "business" functionality for many intents (for example, the "download" operation in the UI involves leveraging the backend to: (1) create a new Feed with the data to be downloaded; (2) attach a "zip" plugin to that feed; (3) monitor the progress; (4) inform the user when complete). First, this arguably extremely useful client-side feature is now locked away in the ChRIS UI, and other clients need to re-implement this again *de novo*. Secondly, the state management is fragile being handled by a web-app client: what happens if the ChRIS UI is closed, crashes, etc while it is managing this intent?

This suggests *Obvious shallow solution #2: Push business logic to CUBE* -- which rests on the very reasonable logic that certain client side *intents* could (or should) be pushed to the backend. After all, the backend is the ultimate heart of ChRIS, the ultimate arbitrator of behavior and functionality.

````
                  ┌──────────────────────────────────────────────┐
                  │                    ChRIS UI                  │
                  ├───────────────────────┬──────────────────────┤
                  │     Visualization     │   Business Logic     │
                  │     (stateless)       │     (stateful)       │
                  └───────────┬───────────┴───────────┬──────────┘
                              │                       │
                              ▼                       ▼
          ┌───────────────────┼───────────────────────┴───────────────────┐
          │      REST API     │      Stateful Service                     │
          ├───────────────────┴───────────────────────────────────────────┤
          │                                                               │
          │                                                               │
          │                               CUBE                            │
          │                                                               │
          │                                                               │
          └───────────────────────────────────────────────────────────────┘
````

The use of the word "shallow" here is deliberate. Clients that service intents need simple *stateful* services, while the backend (or rather its API) is *stateless* -- this is *by design*. By a similar logic that the clients should not need to continually re-invent stateful intents in a multitude of programming languages, the backend API being *stateless* is non-ideal for providing stateful operations. This is a classic round-peg-in-square-hole problem. To service *Intents*, the CUBE backend would by necessity need to expose a radically different API, and also now need to act as a stateful orchestrator rather than a responsive stateless server.

Moreover, the space of intents is potentially unbound. This would centralize additional complexity in the backend. Additionally, if the intent space is unbound, so too the possible context space -- should the CUBE API now provide many different possible "dialects" or API patterns? This too seems a solution that moves technical debt accumulation from the client to the backend.

### Subtle solution proposal: a middle side

It seems clear that clients can benefit from calling a stateful "backend", and CUBE functions best when being called to provide stateless primitives. Thus why not a middle stateful service/server? A client just wants to offload some intent to a server. Does it matter if this "backend" server is CUBE or some intermediary? Arguably a client just wants to know what API endpoint to call and what data to POST.

This logic would suggest that the problem of intent service from the *client* perspective is simply a URL and then the solution becomes:

- Implement this in CUBE
- Implement this in a dedicated microservice

#### Implement in CUBE
Since this service will have a different non-<tt>collection+json</tt> API, the main benefit from implementing / exposing in CUBE is code context to internal django data and methods without needing an intermediate http cross communication layer. It does carry the slight risk however of unintended instability in the CUBE server, and requiring rapid updates/changes to CUBE while this is being developed.

#### Implement outside CUBE
In this solution, a new separate (micro)service

