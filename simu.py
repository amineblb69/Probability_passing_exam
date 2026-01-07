from random import randint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def simulate_notes_prob(nb_qst,true_pts=None,false_pts=None):
    final_grade=0
    
    if true_pts is None :
        true_pts=1
    if false_pts is None:
        false_pts=0
    for i in range(0,nb_qst):
        result=randint(0,1)
        if result==0:
            final_grade+=false_pts
            #print(f"The answer to the question No: {i} is False")
        if result==1 :
            final_grade+=true_pts
            #print(f"The answer to the question No: {i} is True")
    return final_grade

def simulation(sims_nb,nb_qst):
    pass_count=0
    sim_nos=[]
    grades=[]
    rlg_means=[]
    for i in range(0,sims_nb):

        grade= simulate_notes_prob(nb_qst)
        if grade >=10:
            pass_count+=1
        sim_nos.append(i)
        grades.append(grade)
        rlg_means.append(np.mean(grades))

    results=pd.DataFrame({
        'Sim No':sim_nos,
        'Grade':grades,
        'Mean':rlg_means
        })

    fig, (ax1,ax2) = plt.subplots(1,2,figsize=(12,5)) 

    ax1.scatter(results['Sim No'],results['Grade'],label='Grades',color='red')
    ax1.plot(results['Sim No'],results['Mean'],label='Mean', color='black')
    ax1.set_title(f'Results Simulation of {sims_nb} tests of {nb_qst} questions')
    ax1.set_xlabel("Number of simulations")
    ax1.set_ylabel("Points")
    ax1.legend()

    counts, bins, patches = ax2.hist(results['Grade'], bins=10, alpha=0.6, label='Histogram')
    mu = results['Grade'].mean()
    sigma = results['Grade'].std()
    x = np.linspace(bins[0], bins[-1], 200)
    bin_width = bins[1] - bins[0]
    scale = len(results['Grade']) * bin_width
    if sigma > 0:
        pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(- (x - mu) ** 2 / (2 * sigma ** 2)) * scale
    else:
        pdf = np.zeros_like(x)
    ax2.plot(x, pdf, color='darkblue', linewidth=2, label=f'Gaussian fit (μ={mu:.2f}, σ={sigma:.2f})')
    ax2.set_title('Histogram Grades Distribution')
    ax2.set_xlabel('Points')
    ax2.set_ylabel('Frequency')
    ax2.legend()

    plt.tight_layout()
    plt.show()

    prob2pass=pass_count/sims_nb
    return results, prob2pass

sim_results, prob2pass = simulation(sims_nb=10000,nb_qst=40)

print(f"Your probability of passing the exam without studying is {prob2pass}")
 
