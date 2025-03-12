from collections import deque

class SjfScheduler:
    # Inicializador (Construtor d classe)
    def __init__ (self):
        self.fila_processos = deque()
        
    def adicionar_processo (self, pid, tempo_exec):
        processo = (pid, tempo_exec)
        self.fila_processos.append (processo)

    def remover_processos (self):
        if self.fila_processos:
            return self.fila_processos.popleft()
        else:
            print ("Nenhum processo para remover! :)")
            return
    
    # Função que simula o comportammento do agendador SJF
    def sjf_scheduling (self):
        fila_processos_prioridade = sorted (self.fila_processos, key=lambda processo: processo[1])
        self.fila_processos = deque (fila_processos_prioridade)

        tempo_atual = 0  
        tempos_espera = {} 
        tempos_retorno = {}  
        
        print ("\nExecução dos processos (SJF):\n")
        
        while self.fila_processos:
            pid, tempo_exec = self.remover_processos() 
            
            tempos_espera[pid] = tempo_atual  
            tempos_retorno[pid] = tempo_atual + tempo_exec  
            
            print (f"Processo {pid} executando... (Tempo: {tempo_atual} -> {tempo_atual + tempo_exec})")
            
            tempo_atual = tempo_atual + tempo_exec 
        
        print ("\nResumo do escalonamento:\n")

        print ("PID | Tempo de espera | Tempo de retorno")
        
        for pid in tempos_espera:
            print (f"{pid:^3} | {tempos_espera[pid]:^15} | {tempos_retorno[pid]:^16}")

scheduler = SjfScheduler()
scheduler.adicionar_processo (1, 8)
scheduler.adicionar_processo (2, 4)
scheduler.adicionar_processo (3, 2)
scheduler.adicionar_processo (4, 6)

scheduler.sjf_scheduling()
