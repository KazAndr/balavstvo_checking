#ifndef EXAMPLE_H
#define EXAMPLE_H

// заголовочный файл класса СppStudio.h
// интерфейс класса
 
// объявление класса
class CppStudio // имя класса
{
private: // спецификатор доступа private
    int day, // день
        month, // месяц
        year; // год
public: // спецификатор доступа public
    CppStudio(int, int, int); // конструктор класса
    void message(); // функция (метод класса) выводящая сообщение на экран
    void setDate(int, int, int); // установка даты в формате дд.мм.гг
    void getDate(); // отобразить текущую дату
}; // конец объявления класса CppStudio

#endif
