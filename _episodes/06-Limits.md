---
title: "Results and Statistical Analysis"
teaching: 0
exercises: 0
questions:
- "How do we interpret the result?"
objectives:
- "Make datacards"
- "Run combine"
- "Plot limits"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

## create datacard

## run Higgs Combine to computer limits

Run the followiing command to install Higgs Combine:
~~~
cd ${CMSSW_BASE}/src
cmsenv
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
cd $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit
git fetch origin
git checkout v9.1.0
scramv1 b clean; scramv1 b # always make a clean build
~~~
{: .language-bash}

To run the Asymptotic frequentist Limits we can use the following command:
~~~
combine -M AsymptoticLimits realistic-counting-experiment.txt
~~~
{: .language-bash}

The program will print the limit on the signal strength r (number of signal events / number of expected signal events) e .g. Observed Limit: r < XXX @ 95% CL , the median expected limit Expected 50.0%: r < XXX, and edges of the 68% and 95% ranges for the expected limits.
The program will also create a ROOT file `higgsCombineTest.AsymptoticLimits.mH120.root` containing a ROOT tree limit that contains the limit values that we will use later to produce limits plots.


> ## Open a script
>
> For this part, open the python script `scripts/run_combine.py` to run over all of the datacards that you produced in the previous exercise and save all the ROOT files in a directory.
{: .checklist}

> ## Discussion 5.1
>
> Why do we use the rateParam `norm` to change the normalization of the signal yield?
> 
{: .discussion}
{% include links.md %}

## Make limit plots

In this exercise, we will use the limits that were saved in ROOT files produced in the previous exercise to calculate the limit on BR(h--> SS) with respect to the LLP mean proper decay lengths

{% include links.md %}

