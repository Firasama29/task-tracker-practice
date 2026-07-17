package src.main.java;

import java.util.List;
import java.util.Scanner;

import static src.main.java.TaskActivities.addTask;
import static src.main.java.TaskActivities.deleteTask;
import static src.main.java.TaskActivities.filterCompletedTasks;
import static src.main.java.TaskActivities.filterIncompleteTasks;
import static src.main.java.TaskActivities.getTasks;
import static src.main.java.TaskActivities.markCompleted;
import static src.main.java.TaskActivities.markInprogress;
import static src.main.java.TaskActivities.updateTask;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        List<Task> tasks = getTasks();
        if (input.equals("add")) {
            add(scan);
        } else if (input.equals("list")) {
            System.out.println("tasks: " + tasks);
        } else if (input.equals("update")) {
            update(scan, tasks);
        } else if (input.equals("delete")) {
            delete(scan);
        } else if (input.equals("progress")) {
            setInprogress(scan);
        } else if (input.equals("completed")) {
            setCompleted(scan);
        } else if (input.equals("pending")) {
            System.out.println("pending tasks: " + filterIncompleteTasks());
        } else if (input.equals("done")) {
            System.out.println("pending tasks: " + filterCompletedTasks());
        }
    }

    private static void add(Scanner scan) {
        System.out.println("enter the new task: ");
        String newTask = scan.nextLine();
        addTask(newTask);
    }

    private static void update(Scanner scan, List<Task> tasks) {
        System.out.println(tasks);
        System.out.println("enter the id:\n");
        int id = scan.nextInt();
        System.out.println("enter the new task name:\n");
        String updatedTask = scan.next();
        updateTask(id, updatedTask);
    }

    private static void delete(Scanner scan) {
        System.out.println("enter the id:\n");
        int id = scan.nextInt();
        deleteTask(id);
    }

    private static void setInprogress(Scanner scan) {
        System.out.println("enter the id:\n");
        int id = scan.nextInt();
        markInprogress(id);
    }

    private static void setCompleted(Scanner scan) {
        System.out.println("enter the id:\n");
        int id = scan.nextInt();
        markCompleted(id);
    }
}
