---
layout: post
title: "Revisiting joint decoding based multi-talker speech recognition with DNN acoustic model"
date:  2022-03-25 22:20:59 +00:00
image: /images/joint_decoding.jpg
categories: research
authors: "<b>Martin Kocour</b>, Kateřina Žmolíková, Francois Antoine Lucas Yang Ondel, Ján Švec, Marc Delcroix, Tsubasa Ochiai, Lukáš Burget, Jan Černocký"
venue: "INTERSPEECH, Incheon, KR"
website: "https://www.isca-archive.org/interspeech_2022/kocour22_interspeech.html"
slides: /pdfs/2022_IS_multi_talker_speech_recognition_prez.pdf
---
In typical multi-talker speech recognition systems, a neural network-based acoustic model predicts senone state posteriors for each speaker. These are later used by a single-talker decoder which is applied on each speaker-specific output stream separately. In this work, we argue that such a scheme is sub-optimal and propose a principled solution that decodes all speakers jointly. We modify the acoustic model to predict joint state posteriors for all speakers, enabling the network to express uncertainty about the attribution of parts of the speech signal to the speakers. We employ a joint decoder that can make use of this uncertainty together with higher-level language information. For this, we revisit decoding algorithms used in factorial generative models in early multi-talker speech recognition systems. In contrast with these early works, we replace the GMM acoustic model with DNN, which provides greater modeling power and simplifies part of the inference. We demonstrate the advantage of joint decoding in proof of concept experiments on a mixed-TIDIGITS dataset.
