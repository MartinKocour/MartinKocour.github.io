---
layout: post
title: "Delayed Fusion: Integrating Large Language Models into First-Pass Decoding in End-to-end Speech Recognition"
date:  2025-03-25 22:20:59 +00:00
image: /images/delayed_fusion.jpg
categories: research
authors: "Takaaki Hori, <b>Martin Kocour</b>, Adnan Haider, Erik McDermott"
venue: "ICASSP 2025, Hyderabad, IN"
url: "https://2025.ieeeicassp.org/"
---
Delayed fusion incorporates LLM scores into the first-pass ASR hypotheses with a delay during decoding, significantly reducing the number of LLM inference calls. Unlike standard LM fusion mechanisms, delayed fusion enables the use of different tokenizers. Our experiments with OpenLLaMA 7B and Mistral 7B LLMs demonstrate that delayed fusion outperforms traditional N-best rescoring approaches.
