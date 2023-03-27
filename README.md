# Detecting Outdated Screenshot in App Document

## Project summary

In this paper, we propose an approach called DOSAD, *i.e.*, <u>D</u>etecting <u>O</u>utdated <u>S</u>creenshots in <u>A</u>pp <u>D</u>ocument. DOSAD is the first approach that is able to identify whether a screenshot is outdated or not in application documents. To handle the challenge of enumerating screenshots, given an app, DOSAD installs its brand new version and outdated versions on a local device, and uses a GUI testing technique to enumerate their screenshots. To handle the challenge of understanding subtle differences, we train a classifier based on our collected screenshots. After its classifier is trained, given a screenshot of a document, DOSAD can predict whether it is outdated or not.

## Repository

The folder "code": the source code, including our *App Screenshot Extractor*, *Document Screenshot Extractor*, *Screenshot Classifier*, program for drawing figures and other components.

The folder "dataset": the dataset of all captured screenshots used in our EVALUATION ON BENCHMARK.

The folder "real_bugs" and the file "real_bugs.md": details of 20 detected real bugs (EVALUATION IN THE WILD).
