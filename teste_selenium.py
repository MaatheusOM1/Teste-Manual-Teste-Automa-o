import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from time import sleep

def testar_busca_e_carrinho():
    navegador = webdriver.Chrome()
    navegador.get("https://www.advantageonlineshopping.com/#/")
    navegador.maximize_window()

    try:
        inicio_tempo = time.time()
        caixa_busca = WebDriverWait(navegador, 20).until(
            EC.element_to_be_clickable((By.ID, "search"))
        )
        caixa_busca.click()
        print(f"Web: Caixa de busca clicada em {time.time() - inicio_tempo:.2f} segundos.")

        campo_pesquisa = WebDriverWait(navegador, 20).until(
            EC.presence_of_element_located((By.ID, "autoComplete"))
        )

        campo_pesquisa.send_keys("HP CHROMEBOOK 14 G1(ES)")  # Produto escolhido para teste
        time.sleep(2)  # Espera para sugestões carregarem

        try:
            sugestoes = WebDriverWait(navegador, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "autoCompleteItem"))
            )
            print("Web: Sugestões de pesquisa carregadas.")
        except TimeoutException:
            print("Web: Nenhuma sugestão carregada, tentando pressionar ENTER diretamente.")

        campo_pesquisa.send_keys(Keys.RETURN)
        print("Web: Produto buscado.")
        time.sleep(5)

        # Tenta clicar no produto, lidando com o erro de elemento não encontrado
        for _ in range(3):
            try:
                produto_resultado = WebDriverWait(navegador, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'HP CHROMEBOOK 14 G1(ES)')]"))
                )
                produto_resultado.click()
                print("Web: Produto clicado na lista de sugestões.")
                break  # Sai do loop se der certo
            except StaleElementReferenceException:
                print("Elemento não encontrado. Tentando novamente...")

        # Aguarda o botão "Adicionar ao Carrinho"
        botao_adicionar_carrinho = WebDriverWait(navegador, 20).until(
            EC.element_to_be_clickable((By.NAME, "save_to_cart"))
        )
        botao_adicionar_carrinho.click()
        print("Web: Produto adicionado ao carrinho.")

        # Abre o carrinho
        link_carrinho = WebDriverWait(navegador, 20).until(
            EC.element_to_be_clickable((By.ID, "shoppingCartLink"))
        )
        link_carrinho.click()
        print("Web: Carrinho aberto.")

        # Verifica se o produto está no carrinho
        produto_carrinho = WebDriverWait(navegador, 20).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'HP CHROMEBOOK 14 G1(ES)')]"))
        )

        if produto_carrinho:
            print("Produto escolhido 'HP CHROMEBOOK 14 G1(ES)' encontrado no carrinho!")
        else:
            print("Produto escolhido 'HP CHROMEBOOK 14 G1(ES)' não encontrado no carrinho.")

    except TimeoutException as e:
        print(f"Tempo limite ao buscar elemento: {e}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        sleep(15)
        navegador.quit()

testar_busca_e_carrinho()
