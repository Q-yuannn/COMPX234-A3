# COMPX234-A3: Tuple Space Client-Server System
## Overview
This project implements a multi-threaded TCP-based client-server system that simulates a tuple space. Clients can PUT, READ, or GET key-value pairs from a central server. The server handles multiple clients concurrently and maintains operation statistics in real-time.

This system follows the specifications for Assignment 3 of COMPX234 (2025).

## Features
### Server
Maintains a shared tuple space (key: value) with thread-safe operations.

Supports three operations:

READ(k): Returns the value if key k exists.

GET(k): Returns and removes the value if key k exists.

PUT(k,v): Adds (k,v) if key does not exist.

Responds to clients using a defined message format.

Prints statistics every 10 seconds: tuple count, average sizes, client count, and operation counts.

Handles concurrent clients using threads and locks.

### Client
Reads commands from a request file (client_i.txt).

Sends each request to the server synchronously.

Displays the response for each operation.

Handles up to 10 clients in parallel via threads.
## Output examples
### server output
tuples number: 47

average key size: 10.702127659574469

average value size: 5.425531914893617

average tuple size: 16.127659574468087

total operations count: 499937

read count: 166556

get count: 166667

put count: 166714

error count: 500063

client count: 10
### clients output
READ baby_doc : ERR baby_doc does not exist

READ maeterlinck : OK ('maeterlinck', 'Belgian') read

PUT xanthoma_multiplex widespread xanthomas (especially on elbows and knees); often associated with a disorder of lipid metabolism: OK ('xanthoma_multiplex', 'widespread') added

PUT urinate pass after the manner of urine: ERR urinate already exists

GET impudent : ERR impudent does not exist

PUT genus_hyssopus Eurasian genus of perennial herbs or subshrubs: OK ('genus_hyssopus', 'Eurasian') added

READ impressed : ERR impressed does not exist

PUT gene_mutation (genetics) a mutation due to an intramolecular reorganization of a gene: ERR gene_mutation already exists
