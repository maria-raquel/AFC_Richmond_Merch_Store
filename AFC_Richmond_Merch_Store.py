import f_manipulacao as fm
import f_print as fp
import f_input as fi

fp.boas_vindas()
escolha = fi.opcao_menu_principal()

while escolha:

    # Compras
    if escolha == 1:
        escolha_compras = fi.opcao_menu_compras()

        while escolha_compras:

            # Compras - Nova compra
            if escolha_compras == 1:
                fm.nova_compra()

            # Compra - Busca
            elif escolha_compras == 2:
                fm.buscar_compra()

            # Compra - Atualizar
            elif escolha_compras == 3:
                fm.atualizar_compra()

            # Compra - Cancelar
            elif escolha_compras == 4:
                fm.cancelar_compra()

            escolha_compras = fi.opcao_menu_compras()

    # Produtos
    elif escolha == 2:
        escolha_produto = fi.opcao_menu_produto()

        while escolha_produto:

            # Produtos - Cadastrar
            if escolha_produto == 1:
                fm.cadastrar_produto()

            # Produtos - Buscar
            elif escolha_produto == 2:
                fm.buscar_produto()
                pass

            # Produtos - Atualizar
            elif escolha_produto == 3:
                fm.atualizar_produto()

            # Produtos - Remover
            elif escolha_produto == 4:
                fm.remover_produto()
                
            escolha_produto = fi.opcao_menu_produto()

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
