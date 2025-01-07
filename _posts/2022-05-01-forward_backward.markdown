---
layout: post
title: "GPU-Accelerated Forward-Backward Algorithm with Application to Lattice-Free MMI"
date:  2022-03-25 22:20:59 +00:00
image: /images/forward_backward.jpg
categories: research
authors: "Francois Antoine Lucas Yang Ondel, L'ea-Marie Lam-Yee-Mui, <b>Martin Kocour</b>, Filippo Caio Corro, Lukáš Burget"
venue: "ICASSP, Singapore, SG"
website: "https://ieeexplore.ieee.org/document/9746824"
arxiv: "https://arxiv.org/abs/2112.00709"
slides: /pdfs/2022_ICASSP_gpu_accelerated_forward_backward_prez.pdf
---
In this work we propose to express the forward-backward algorithm in terms of operations between sparse matrices in a specific semiring.
This new perspective naturally leads to a GPU-friendly algorithm which is easy to implement in Julia or any programming languages with native support of semiring algebra.
We use this new implementation to train a TDNN with the LF-MMI objective function and we compare the training time of our system with PyChain -- a recently introduced C++/CUDA implementation of the LF-MMI loss. Our implementation is about two times faster on GPU than PyChain implementation.