package Урок_2;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

public class ToyStoreRaffle {

    // Хранилище игрушек и их весов
    private static Map<String, Double> toys = new HashMap<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nВыберите действие:");
            System.out.println("1. Добавить новую игрушку");
            System.out.println("2. Выбрать игрушку");
            System.out.println("3. Выйти из программы");

            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    addAgame(scanner);
                    break;
                case "2":
                    if (toys.isEmpty()) {
                        System.out.println("Сначала добавьте игрушки.");
                    } else {
                        chooseAgame();
                    }
                    break;
                case "3":
                    System.out.println("Программа завершена.");
                    System.exit(0);
                default:
                    System.out.println("Неверный ввод. Пожалуйста, выберите правильное действие.");
            }
        }
    }

    private static void addAgame(Scanner scanner) {
        System.out.print("Введите название игрушки: ");
        String title = scanner.nextLine();
        System.out.print("Введите вес игрушки (в килограммах): ");
        double weight = scanner.nextDouble();
        toys.put(title, weight);
        System.out.printf("Игрушка '%s' с весом %.2f кг успешно добавлена!%n", title, weight);
        scanner.nextLine(); // Считываем лишний перевод строки
    }

    private static void chooseAgame() {
        double summaVesov = toys.values().stream().mapToDouble(Double::doubleValue).sum();
        double RandomlCalculated = new Random().nextDouble() * summaVesov;

        double CurrentSum = 0;
        for (Map.Entry<String, Double> entry : toys.entrySet()) {
            CurrentSum += entry.getValue();
            if (CurrentSum >= RandomlCalculated) {
                System.out.printf("Вы выбрали игрушку: %s%n", entry.getKey());
                return;
            }
        }
    }
}