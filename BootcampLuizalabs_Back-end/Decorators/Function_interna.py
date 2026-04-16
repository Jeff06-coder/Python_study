def todas():
    print("Todas as funções decoradas")
    def ola():
        print("Olá, mundo!")

    def tchau():
        print("Tchau, mundo!")

    ola()
    tchau()

todas()