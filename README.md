# tudoweb-pesquisa-python

Aplicação CLI em Python estruturada com loops de repetição, condicionais de validação de dados e persistência em memória para relatórios de feedback.

Este projeto consiste em um programa desenvolvido em Python para coletar e exibir os dados de uma pesquisa de opinião com os clientes da empresa de marketing **TudoWeb**. O objetivo principal é avaliar o grau de satisfação dos usuários em relação ao atendimento prestado.

## 🚀 Objetivo do Projeto

Desenvolver uma aplicação de linha de comando (CLI) que utiliza estruturas de repetição e condicionais em Python para coletar informações demográficas e feedbacks dos clientes de forma automatizada e organizada.

## 📋 Funcionalidades e Regras do Sistema

O programa solicita as seguintes informações para um total fixo de **10 entrevistados**:
* **Nome** do cliente;
* **Idade** do cliente;
* **Opinião sobre o atendimento**, seguindo a escala numérica:
  * `1` - Excelente
  * `2` - Boa
  * `3` - Ruim
 
  ### 📊 Relatório Final Gerado
Ao final das 10 interações, o sistema consolida e exibe as métricas acumuladas:
* Quantidade total de avaliações **Excelente** (`1`);
* Quantidade total de avaliações **Ruim** (`3`).

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** [Python 3](https://python.org)
* **Estruturas de Lógica:** 
  * Estrutura de repetição (`for i in range(1, 11)`) para controlar o limite exato de 10 entrevistas.
  * Estruturas condicionais (`if`, `elif`) para incremento dos contadores de opinião baseados nas respostas dos clientes.


