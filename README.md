# permeability_mpd
Python code to calculate permeability using mean penetration depth as discussed in the paper : Nan, Tongchao &amp; Wu, Jichun &amp; Li, Kaixuan &amp; Jiang, Jianguo. (2019). Permeability Estimation Based on the Geometry of Pore Space via Random Walk on Grids. Geofluids. 2019. 10.1155/2019/9240203. (https://www.hindawi.com/journals/geofluids/2019/9240203/)

In this paper, there is a flowchart given (figure 3). Based on this, the mean penetration depth (D<sub>G</sub>) for a parallel plate system was calcuated. The permeability(k) of the system can thus be estimated as k=CD<sub>G</sub><sup>2</sup>. Where C is a constant that depends on the geometry and porosity of the medium.

The rwalk.py file is for calculating the penetration depth for a particular plate seperation. A plot can be generated for different penetration depth values for different plate seperations. From the slope of the plot, mean penetration depth can be calculated.

The rwalkp.py file is for generating a text file showing the co-ordinate of the particle after each iteration so that the trajectory of the particle can be plotted.
