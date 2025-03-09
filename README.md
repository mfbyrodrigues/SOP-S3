# Introdução a Sistemas Operacionais - Curso Técnico em Informática

Este repositório contém os materiais e exercícios da disciplina de **Sistemas Operacionais** do curso técnico integrado em Informática. Aqui, organizo códigos, anotações e práticas para acompanhar o aprendizado dos conceitos de sistemas operacionais, utilizando a linguagem Python.

## Índice

- [Sobre a matéria](#sobre-a-materia)
- [Conteúdo programático](#conteudo-programatico)
- [Configuração do ambiente](#configuracao-do-ambiente)
- [Minhas anotações](#minhas-anotacoes)
- [Referências](#referencias)

## Sobre a matéria

A disciplina de **Sistemas Operacionais** tem como objetivo ensinar os principais conceitos de funcionamento e gerenciamento de sistemas computacionais, com foco em gerenciamento de processos, memória, armazenamento, e sistemas de arquivos. Vamos utilizar a linguagem Python para simular e entender o funcionamento de várias funcionalidades típicas dos sistemas operacionais modernos.

## Conteúdo programático

Os principais tópicos abordados incluem:

### 1. **Fundamentos de Sistemas Operacionais**
   - O que é um sistema operacional?
   - Funções básicas de um sistema operacional.
   - Tipos de sistemas operacionais (monolíticos, microkernels, etc.)

### 2. **Gerenciamento de Processos**
   - O que são processos e threads?
   - Criação e execução de processos em Python (utilizando a biblioteca `os` e `multiprocessing`).
   - Gerenciamento de processos com **Pipes**, **Filas** e **Fila de Prioridade**.
   - Sincronização de processos (Exemplo: uso de semáforos e mutex).
   
### 3. **Gerenciamento de Memória**
   - Memória virtual e física.
   - Alocação de memória (mapeamento de memória em Python).
   - Gerenciamento de heap e stack.

### 4. **Gerenciamento de Entrada/Saída (I/O)**
   - Manipulação de arquivos e diretórios com Python (`os`, `shutil`, `pathlib`).
   - Buffer de leitura/escrita e controle de dispositivos de I/O.

### 5. **Gerenciamento de Arquivos**
   - Sistema de arquivos e estrutura de diretórios.
   - Operações com arquivos e permissões de acesso.
   - Simulação de sistemas de arquivos (usando a biblioteca `os`).
   - Implementação de comandos básicos de terminal como `ls`, `cp`, `mv`, `rm`.

### 6. **Sistemas de Arquivos e Dispositivos**
   - Gerenciamento de dispositivos e drivers.
   - Introdução a dispositivos de armazenamento (HDD, SSD).
   - Criando um sistema simples de gerenciamento de arquivos e diretórios com Python.

### 7. **Escalonamento de Processos**
   - Algoritmos de escalonamento (Round Robin, FIFO, Prioridade, etc).
   - Simulação de escalonamento com Python.

### 8. **Segurança e Controle de Acesso**
   - Controle de permissões de arquivos e diretórios.
   - Simulação de controle de acesso a recursos do sistema operacional.
   - Gestão de usuários e grupos em Python.

### 9. **Sistemas Distribuídos e Redes**
   - Comunicação entre processos e sistemas distribuídos (exemplo de sockets).
   - Simulação de servidores e clientes utilizando Python.
   
### 10. **Projeto Prático**
   - Desenvolvimento de uma aplicação simples de sistema operacional utilizando conceitos aprendidos.
   - Implementação de um sistema simples de gerenciamento de arquivos, processos e escalonamento.

## Configuração do ambiente

Para acompanhar as aulas e praticar, estou utilizando:

- **Linguagem:** Python 3.x
- **IDE:** Visual Studio Code ou PyCharm
- **Bibliotecas auxiliares:** `os`, `multiprocessing`, `threading`, `socket`, `shutil`, `pathlib`

## Minhas anotações

Aqui adicionarei anotações e códigos feitos conforme avanço na disciplina. 

## Referências

- Documentação oficial do Python (https://docs.python.org/3/)
- Livros recomendados sobre Sistemas Operacionais:
  - **"Operating System Concepts"** de Silberschatz, Galvin e Gagne.
  - **"Modern Operating Systems"** de Andrew Tanenbaum.
- Aulas práticas fornecidas pelo professor da disciplina.

---

Esse repositório servirá como meu espaço de aprendizado e consulta ao longo da disciplina, onde poderei acessar tanto exemplos práticos quanto anotações de teoria para melhor compreender o funcionamento dos sistemas operacionais e suas interações com a programação em Python.
