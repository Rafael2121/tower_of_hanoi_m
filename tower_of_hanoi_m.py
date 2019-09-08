import copy

class knowledge:
    changed = None

    def head(self):
        """
        O objetivo é mudar a posição dos discos do primeiro pino para qualquer outro.
        Inicialmente os discos estão ordenados de 1 -> N no primeiro pino.
        ex:
        [1]  |   |
        [2]  |   |
        [3]  |   |
        +++++++++++
        Regras do jogo:
        (1) Um pino de valor maior não pode ficar acima de um de valor menor.
            ex: pino 2 e 3 não podem ficar acima do pino 1; 3 não pode ficar acima do 2, etc... 
        
        Exmplo de objetivo:
        |   [1]   |
        |   [2]   |
        |   [3]   |
        +++++++++++
        """
        ##### QUANTIDADE DE DISCOS
        self.discs_num = 9
        ##########################
        platform = []
        platform.append(list(range(self.discs_num , 0, -1)))
        for i in range(2):
            platform.append([])
        platform = self.hanoi_tower_instance(platform, 0)
        print("End")

    def hanoi_tower_instance(self, platform, this_pos):
        """ Este método constroi e atua acima de cada instância que resolverá a torre
        Cada instancia tem direito de movimentar um disco, esta cria uma cópia da mesa,
         verifica as possibilidades com aquele disco, faz a PRIMEIRA mudança possível e
         passa para a próxima isntancia
        Ponto crítico:
        - Caso a isntancia esteja em uma posição que não tem movimentações, é incrementado
         a sua posição para verificação, TODAS INSTANCIA DEVEM MOVIMENTAR, entretando uma
         que esteja com a solução deve somente retorna-lá
        """
        local_platform = copy.deepcopy(platform)
        if self.stop_condition(local_platform):
            #  Caso esta isntancia atenda a solução, retorna imediatamente o valor desta
            return local_platform
        while True:
            possibilites = self.verify_possibilites(local_platform, this_pos)
            if possibilites == []:
                this_pos = this_pos + 1 if this_pos < 2 else 0
            else: 
                break
        t = possibilites[0] # Pega e executa a primeira possibilidade de troca
        local_platform = self.switch_disc(local_platform, this_pos, t[0])
        self.print_tower(local_platform)
        return self.hanoi_tower_instance(local_platform, this_pos)


    def verify_possibilites(self, platform, position):
        """ Verifica todas possibilidades de acordo com aquele estado
            Ponto crítico: 
            - Plataformas vazias não tem possibilidade de movimentação
            - Plataformas com um disco recentemente movimentado não deverão fazer 
             SWAP(não faz sentido mudar de local um disco que acabou de ser alocado)
            - Ignora pinos que tem discos com valores menores doque o que estou 
             verificando
         """
        plat_possibilites = []
        p_list = self.next_positions(position)
        if len(platform[position]) == 0 or platform[position][-1] == self.changed:
            return []
        else:
            item = platform[position][-1]
            for p in p_list:
                p_disc = platform[p][-1] if len(platform[p]) > 0 else 0
                if p_disc == 0 or (p_disc != 0 and p_disc > item):
                    plat_possibilites.append((p, p_disc))
            return plat_possibilites

    def next_positions(self, position):
        """Constrói uma lista com as próximas posições a serem observadas 
         de acordo com um ponto específico"""
        t = list(range(3))
        t.remove(position)
        if position == 1:
            t.reverse()
        return t 

    def stop_condition(self, platform):
        """ Verifica se a plataforma atual atende as condições de parada."""
        s = list(range(self.discs_num , 0, -1))
        if platform[1] == s or platform[2] == s:
            return True
        return False

    def switch_disc(self, platform, current_pos, destination_pos):
        """ Faz a troca de posição do disco, retirando a pilha atual a o inserindo em outra
        pop para retirar ultimo e append para inserir ao último
        """
        disc = platform[current_pos].pop()
        platform[destination_pos].append(disc)
        self.changed = disc # Salva na memória do algoritmo qual foi o último disco a ser movimentados
        return platform

    def print_tower(self, platform):
        """ Printa a torre de uma maneira mais "amigável" """
        for i in range(self.discs_num , 0, -1):
            for f in range(3):
                disc = "[{}]".format(platform[f][i-1]) if len(platform[f]) >= i else " | "
                print(" {} ".format(disc), end="")
            print("")
        print("++++++++++++++")


if __name__ == "__main__":
    hanoi = knowledge()
    hanoi.head()