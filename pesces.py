
def calc_bayes(prio_A, prob_B_dado_A, prob_B):
    return (prio_A * prob_B_dado_A) / prob_B

if __name__ == '__main__':
    prob_azul = 40 / 100
    prob_hembra_dado_azul = 70 / 100
    prob_rojo = 60 /100
    prob_hembra_dado_rojo = 40 /100 
    prob_de_hembra = (prob_azul * prob_hembra_dado_azul) + (prob_rojo * prob_hembra_dado_rojo)
    probabilidad = round(calc_bayes(prob_azul, prob_hembra_dado_azul, prob_de_hembra), 3) 
    total = round(probabilidad * 100, 2)
    print(f'{total} %')