import f_input as fi
import f_manipulacao as fm
import f_print as fp

fp.boas_vindas()
escolha = fi.opcao_menu_principal()

while escolha != '0':

    # Compras
    if escolha == '1':
        escolha_compras = fi.opcao_menu_compras()
        while escolha_compras != '0':

            # Compras - Nova compra
            if escolha_compras == '1':
                fm.nova_compra()

            # Compra - Busca
            elif escolha_compras == '2':
                fm.buscar_compra()

            # Compra - Atualizar
            elif escolha_compras == '3':
                fm.atualizar_compra()

            # Compra - Cancelar
            elif escolha_compras == '4':
                fm.cancelar_compra()

            escolha_compras = fi.opcao_menu_compras()

    # Produtos
    elif escolha == '2':
        escolha_produto = fi.opcao_menu_produto()
        while escolha_produto != '0':

            # Produtos - Cadastrar
            if escolha_produto == '1':
                fm.cadastrar_produto()

            # Produtos - Buscar
            elif escolha_produto == '2':
                fm.buscar_produto()
                pass

            # Produtos - Atualizar
            elif escolha_produto == '3':
                fm.atualizar_produto()

            # Produtos - Remover
            elif escolha_produto == '4':
                fm.remover_produto()

            escolha_produto = fi.opcao_menu_produto()

    # Clientes
    elif escolha == '3':
        escolha_cliente = fi.opcao_menu_cliente()
        while escolha_cliente != '0':

            # Clientes - Cadastrar
            if escolha_cliente == '1':
                fm.cadastrar_cliente()

            # Clientes - Buscar
            elif escolha_cliente == '2':
                fm.buscar_cliente()

            # Clientes - Atualizar
            elif escolha_cliente == '3':
                fm.atualizar_cliente()
            
            # Clientes - Remover
            elif escolha_cliente == '4':
                fm.apagar_cliente()

            escolha_cliente = fi.opcao_menu_cliente()

    # Vendedores
    elif escolha == '4':
        escolha_vendedor = fi.opcao_menu_vendedor()
        while escolha_vendedor != '0':

            # Vendedores - Cadastrar
            if escolha_vendedor == '1':
                fm.cadastrar_vendedor()

            # Vendedores - Buscar
            elif escolha_vendedor == '2':
                fm.buscar_vendedor()

            # Vendedores - Atualizar
            elif escolha_vendedor == '3':
                fm.atualizar_vendedor()

            escolha_vendedor = fi.opcao_menu_vendedor()

    # Relatórios
    elif escolha == '5':
        fm.relatorio()
    
    escolha = fi.opcao_menu_principal()

fp.despedida()