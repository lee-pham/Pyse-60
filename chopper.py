# -*- coding: utf-8 -*-
data = """␛="<MCE CRT Display Option␛=$BMain Menu␛)␛=*4F1  -  Job Configuration Parameters␛=,4F2  -  Performance Reports Menu␛=.4F3  -  Graphic Display of Elevator Status␛=04F4  -  Main Menu␛=24F5  -  CRT Terminal Initialization␛=44F6  -  Computer Parameters␛=64F7  -  Special Event Calendar Menu␛=84F8  -  Car  A  Inputs and Outputs␛=8? A ␛=:.Shift F2  -  System Performance Counters␛=<.Shift F5  -  Security Menu␛=>.Shift F6  -  CMS Parameters␛(␛H␂␛=',2::::::::::::::::::::::::::::::::::::::::::::::::::::::::::3␛=(*2::::::::::::::::::::::::::::::::::::::::::::::::::::::::::3 6␛=)*6␛=)e6 6␛=**6␛=*e6 6␛=+*6␛=+e6 6␛=,*6␛=,e6 6␛=-*6␛=-e6 6␛=.*6␛=.e6 6␛=/*6␛=/e6 6␛=0*6␛=0e6 6␛=1*6␛=1e6 6␛=2*6␛=2e6 6␛=3*6␛=3e6 6␛=4*6␛=4e6 6␛=5*6␛=5e6 6␛=6*6␛=6e6 6␛=7*6␛=7e6 6␛=8*6␛=8e6 6␛=9*6␛=9e6 6␛=:*6␛=:e6 6␛=;*6␛=;e6 6␛=<*6␛=<e6 6␛==*6␛==e6 6␛=>*6␛=>e6 6␛=?*6␛=?e6 6␛=@*1::::::::::::::::::::::::::::::::::::::::::::::::::::::::::5␋:5␛H␃␛=@+ Ver 3.64 EMI A-2K␛G|␛A38␛F03/08/17 16:38:14        F4 = Main Menu"""
parsed = data.split("␛")
print(data)
print(parsed)
for i in range(0, len(parsed)):
    print(parsed[i])
