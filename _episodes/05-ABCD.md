---
title: "Background Estimation"
teaching: 0
exercises: 0
questions:
- "What are the source of background for MDS?"
- "How do we estimate the background contribution?"
objectives:
- "Understand background sources for MDS"
- "Understand ABCD method"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

As you've seen in the previous exercise, the main background is from clusters produced in pilup interactions.
To estimate the background, we use a fully data-driven background estimation method, the ABCD method, that make use of two variables that are independent for the background: $N_{\text{hits}}$ and $\Delta\phi\text{(cluster, MET)}$.

To validate that the two variables are independent for the background, we create two validation region that are enriched with background and perform ABCD method to check that the prediction from ABCD matches with the observation.


> ## Open a notebook
>
> For this part, open the notebook called `ABCD_validation.ipynb` and define the OOT control region and perform the validation test for various thresholds.
{: .checklist}


{% include links.md %}

