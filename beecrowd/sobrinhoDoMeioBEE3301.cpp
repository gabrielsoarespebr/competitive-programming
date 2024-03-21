// platform: beecrowd - https://judge.beecrowd.com/pt/problems/view/3301
// programming language: C++
// status: Accepted

// author: Gabriel Soares
// https://www.linkedin.com/in/gabrielsoarespebr/
// https://github.com/gabrielsoarespebr

#include <iostream>

using namespace std;

int main()
{
    const int tamanho = 3;
    int max = 0;
    int min = 10000;
    int index;
    int idadeLista[tamanho];
    const char *nomeLista[tamanho] = {"huguinho", "zezinho", "luisinho"};

    for (int i = 0; i < tamanho; i++)
    {
        cin >> idadeLista[i];

        if (idadeLista[i] > max)
        {
            max = idadeLista[i];
        };

        if (idadeLista[i] < min)
        {
            min = idadeLista[i];
        };
    }

    for (int i = 0; i < tamanho; i++)
    {
        if ((idadeLista[i] != max) && (idadeLista[i] != min))
        {
            index = i;
            break;
        };
    }

    cout << nomeLista[index] << endl;

    return 0;
}