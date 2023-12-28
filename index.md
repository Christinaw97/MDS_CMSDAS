---
layout: lesson
root: .  # Is the only page that doesn't follow the pattern /:path/index.html
permalink: index.html  # Is the only page that doesn't follow the pattern /:path/index.html
---

<!-- this is an html comment -->

{% comment %} This is a comment in Liquid {% endcomment %}

<a href="{{ page.root }}/fig/CMS-EXO-20-015_Figure-aux_004-a.png">
  <img src="{{ page.root }}/fig/CMS-EXO-20-015_Figure-aux_004-a.png" alt="event display" height=420 width=600 />
</a>

> ## Links
> 
> * [CMSDAS at LPC2024](https://indico.cern.ch/event/1333922/)
{: .callout}

> ## Prerequisites
>
> * [CMS DAS Pre-exercises](https://fnallpc.github.io/cms-das-pre-exercises/) 
{: .prereq}


### Goal of this exercise

This analysis will search for long-lived particles decaying in the muon detector, creating a particle shower with a large hit multiplicity. 

The exercise is performed on data collected during Run 2. 

Students will study general features of long-lived particles, including:
 * studying the reconstruction efficiency;
 * making event displays;
 * optimize the event selection;
 * estimate background yield with the ABCD method;
 * set limit on the LLP cross section.

### Facilitators CMSDAS LPC 2024

 * Martin Kwok (FNAL)
 * Christina Wang (Caltech)
 * Daniel Guerrero (FNAL)
 * Daniel Diaz (UCSD)
 * Michael Carrigan (OSU)
 * Pallabi Das (Princeton)	

### Introductory slides

We will start with this version of slides: [FIXME.pdf](). (FIXME)

### Support

Join the [LongEX LLP Mattermost channel](https://mattermost.web.cern.ch/cmsdaslpc2024/channels/longexllp) and don't hesitate to ask for help from the facilitators in the room.


{% include links.md %}
