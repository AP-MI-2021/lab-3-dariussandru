def citire_lista():
    """
    Functia citeste o lista
    :return: lista
    """
    lista = []
    lungime_lista = int(input("Lungimea liste :"))
    nr_element = 1
    while lungime_lista:
        element = int(input(f"Elementul {nr_element} este :"))
        lista.append(element)
        lungime_lista = lungime_lista - 1
        nr_element = nr_element + 1
    return lista


def nr_prim(nr):
    """
    :param nr: numarul pe care il verificam daca este prim
    :return: true daca nr este prim si false in caz contrar
    """
    if nr < 2:
        return False
    for i in range(2, nr):
        if nr % i == 0:
            return False
    return True


def test_nr_prim():
    """
    Functie test pentru functia nr_prim
    """
    assert nr_prim(13) == True
    assert nr_prim(12) == False
    assert nr_prim(14) == False


def get_longest_all_primes(lista_principala):
    """
    Functie care determina cea mai lunga subsecventa in care toate numerele sunt prime
    :param lista_principala:
    :return:
    """
    lungime_max = 0
    lungime_actual = 0
    secv_max = []
    secv_act = []
    for n in lista_principala:
        if nr_prim(n):
            lungime_actual = lungime_actual + 1
            secv_act.append(n)
        else:
            if lungime_actual > lungime_max:
                lungime_max = lungime_actual
                secv_max = secv_act

            lungime_actual = 0
            secv_act = []

    if lungime_actual > lungime_max:
        secv_max = secv_act
    return secv_max


def test_get_longest_all_primes():
    """
    Functie de test pentru functia get_longest_all_primes
    :return:
    """
    assert (get_longest_all_primes([1, 5, 7, 12, 7, 3, 5, 19, 15, 2]) == [7, 3, 5, 19])
    assert (get_longest_all_primes([1, 5, 7, 12, 7, 3, 5, 19]) == [7, 3, 5, 19])
    assert (get_longest_all_primes([4, 6, 8, 10, 15, 49]) == [])
    assert (get_longest_all_primes([1, 2, 4, 5, 8, 7]) == [2])


def nr_divizori(nr):
    """
    :param nr: un numar int
    :return: cati divizori are nr
    """
    numar_divizori = 0
    if nr == 1:
        numar_divizori = 1
    else:
        for i in range(2, (nr // 2) + 1):
            if nr % i == 0:
                numar_divizori += 1

    return numar_divizori


def test_nr_divizori():
    assert nr_divizori(6) == 2
    assert nr_divizori(12) == 4


def get_longest_same_div_count(lista_principala):
    """
    Functia determina cea mai lunga secventa co prop. ca numerele au acelas nr de divizori
    :param lista_principala: toata lista de numere
    :return: secventa cea mai lunga cu proprietatea data
    """

    lungime_max = 0
    secv_max = []
    lungime_actuala = 1
    secv_actuala = [lista_principala[0]]
    nrdivizori = nr_divizori(lista_principala[0])

    for n in range(1, len(lista_principala)):
        if nr_divizori(lista_principala[n]) == nrdivizori:
            lungime_actuala += 1
            secv_actuala.append(lista_principala[n])
        else:
            if lungime_actuala > lungime_max:
                lungime_max = lungime_actuala
                secv_max = secv_actuala

            secv_actuala = lista_principala[n]
            lungime_actuala = 1
            nrdivizori = nr_divizori(lista_principala[n])

    return secv_max


def test_get_longest_same_div_count():
    """
    Functia care testeaza functia get_longest_same_div_count
    :return:
    """
    assert (get_longest_same_div_count([6, 8, 10, 9, 25, 2]) == [6, 8, 10])
    assert (get_longest_same_div_count([7, 2, 9, 25]) == [7, 2])
    assert (get_longest_same_div_count([1, 2, 4]) == [1])
    assert (get_longest_same_div_count([6, 9, 25, 49, 10, 8, 2]) == [9, 25, 49])


def main():
    test_nr_prim()
    test_get_longest_all_primes()
    test_nr_divizori()
    test_get_longest_all_primes()
    lista_principala = []
    f = False
    while f != True:
        print("1. Citire data pentru lista")
        print("2. Det. cea mai lunga subsecventa cu proprietatea 1")
        print("3. Det. cea mai lunga subsecventa cu proprietatea 2")
        print("4. Iesire din program")
        print()
        optiune = int(input("Dati obtiunea:"))

        if optiune == 1:
            lista_principala = citire_lista()
            print()
        if optiune == 2:
            secv1 = get_longest_all_primes(lista_principala)
            print(secv1)
            print()
        if optiune == 3:
            secv2 = get_longest_same_div_count(lista_principala)
            print(secv2)
            print()
        if optiune == 4:
            f = True
main()