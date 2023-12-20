import numpy as np
import sys
import math
def weight_calc(llp_ct, new_ctau, old_ctau):
    if llp_ct.ndim > 1:llp_ct = np.array(np.sum(llp_ct,axis=1))
    source = np.exp(-1.0*llp_ct/old_ctau)/old_ctau**2
    weight = 1.0/new_ctau**2 * np.exp(-1.0*llp_ct/new_ctau)/source
    return weight

def make_datacard(outDataCardsDir,modelName,  signal_rate, observation, sig_unc, sig_unc_name):

    assert(len(signal_rate) == len(observation) == 4)
    assert(len(sig_unc_name)==len(sig_unc))
    a,b,c,d = observation[0], observation[1], observation[2], observation[3]
    
    text_file = open(outDataCardsDir+modelName+".txt", "w")

    text_file.write('imax {0} \n'.format(4))
    text_file.write('jmax {0} \n'.format(1))
    text_file.write('kmax * \n')
    text_file.write('shapes * * FAKE \n')

    text_file.write('--------------- \n')
    text_file.write('--------------- \n')
    text_file.write('bin \t chA \t chB \t chC \t chD \n')
    text_file.write('observation \t {0:6.2f} \t {1:6.2f} \t {2:6.2f} \t {3:6.2f} \n'.format(a, b, c, d))
    text_file.write('------------------------------ \n')
    text_file.write('bin '+'\t chA ' * 2 + '\t chB ' * 2 +'\t chC '* 2 +'\t chD '* 2 +'\n')
    process_name = '\t signal \t bkg '
    text_file.write('process ' + process_name * 4 + '\n')
    process_number = '\t 0 \t 1'
    text_file.write('process ' + process_number * 4 + '\n')
    rate_string = 'rate'
    for x in signal_rate:# 4 bins
        rate_string +='\t {0:e} \t 1 '.format(x)
    text_file.write(rate_string+'\n')
    text_file.write('------------------------------ \n')

    text_file.write('A	 rateParam	 chA	 bkg 	  (@0*@2/@1)			B,C,D \n')
    text_file.write('B	 rateParam	 chB	 bkg 	 {0:.2f}        [0,{1:.2f}] \n'.format(b, b*7)) 
    text_file.write('C	 rateParam	 chC	 bkg 	 {0:.2f}        [0,{1:.2f}] \n'.format(c, c*7)) 
    text_file.write('D	 rateParam	 chD	 bkg 	 {0:.2f}        [0,{1:.2f}] \n'.format(d, d*7)) 
    text_file.write('norm rateParam * signal 1  \n')


  #### uncertainties ####
    for i in range(len(sig_unc_name)):
            unc_text = sig_unc_name[i]+' \t lnN'
            if len(sig_unc[i])==4:#symmetric uncertainties
                for j in range(4):#bin
                    if sig_unc[i][j] == 0.0:unc_text += ' \t -'
                    else: unc_text += ' \t '+str(sig_unc[i][j]+1)
                    unc_text += '\t - '
            elif len(sig_unc[i])==8:#asymmetric
                for j in range(4):#bin A, B, C, D
                    if  sig_unc[i][j] == 0.0 and sig_unc[i][j+4] == 0.0: unc_text += ' \t -'
                    else:unc_text += ' \t {0}/{1}'.format(1-sig_unc[i][j],1+sig_unc[i][j+4])
                    unc_text += '\t -'
            else: assert(False)
            text_file.write(unc_text + ' \n')

    text_file.close()

