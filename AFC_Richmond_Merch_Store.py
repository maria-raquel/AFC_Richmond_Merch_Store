import f_manipulacao as fm
import f_print as fp
import f_input as fi

fp.boas_vindas()
escolha = fi.opcao_menu_principal()

while escolha != 0:

    # Compras
    if escolha == 1:
        escolha_compras = fi.opcao_menu_compras()

        # Compras - Nova compra
        if escolha_compras == 1:
            fm.nova_compra()

        # Compra - Busca
        elif escolha_compras == 2:
            fm.buscar_compra()

        # Compra - Atualizar
        elif escolha_compras == 3:
            pass

        # Compra - Cancelar
        elif escolha_compras == 4:
            pass

        # Voltar
        else:
            pass

    # Produtos
    elif escolha == 2:
        pass

    # Clientes
    elif escolha == 3:
        pass

    # Vendedores
    elif escolha == 4:
        pass

    # Relatórios
    elif escolha == 5:
        pass

    else:
        fp.mensagem_erro()
    
    escolha = fi.opcao_menu_principal()