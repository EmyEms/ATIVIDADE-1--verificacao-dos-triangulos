
---

# Verificação de Semelhança de Triângulos

Este repositório contém um programa em Python que verifica a semelhança entre dois triângulos usando três critérios matemáticos: **LAL (Lado-Ângulo-Lado)**, **AA (Ângulo-Ângulo)** e **LLL (Lado-Lado-Lado)**.

## Descrição

O objetivo deste projeto é determinar se dois triângulos são semelhantes com base nas informações fornecidas sobre seus lados e ângulos. O código é capaz de verificar a semelhança usando três critérios diferentes:

1. **LAL (Lado-Ângulo-Lado)**: Dois lados proporcionais e o ângulo entre eles congruente.
2. **AA (Ângulo-Ângulo)**: Dois ângulos congruentes.
3. **LLL (Lado-Lado-Lado)**: Todos os lados proporcionais.

O programa pede como entrada os três lados e os três ângulos dos dois triângulos e, em seguida, verifica a semelhança.

## Como funciona

- O código usa três funções para verificar os critérios de semelhança (LAL, AA, LLL).
- Dependendo da entrada fornecida, o programa retornará uma mensagem indicando se os triângulos são semelhantes e pelo qual critério.
- Se os triângulos não forem semelhantes por nenhum critério, o programa informará que eles **não são semelhantes**.

## Captura de Tela

Abaixo está uma captura de tela do esboço geométrico feito no **GeoGebra**, mostrando dois triângulos, que foram usados para testar a semelhança no programa:

(https://raw.githubusercontent.com/EmyEms/ATIVIDADE-1--verificacao-dos-triangulos/refs/heads/main/print%20dos%20triangulos.jpeg)

## Link para o GeoGebra

Visualizar o esboço geométrico dos triângulos e suas medidas diretamente no GeoGebra através do link abaixo:

[Link para o GeoGebra](https://www.geogebra.org/calculator/wfxkqmfe)

## Estrutura do Projeto

- **verificar_lal()**: Verifica a semelhança pelo critério Lado-Ângulo-Lado (LAL).
- **verificar_aa()**: Verifica a semelhança pelo critério Ângulo-Ângulo (AA).
- **verificar_lll()**: Verifica a semelhança pelo critério Lado-Lado-Lado (LLL).



   


