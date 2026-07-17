package main.java;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class TaskActivities {

    public static void addTask(String taskName) {
        List<Task> tasks = getTasks();
        Task task;
        if(!tasks.isEmpty()) {
            int maxId = 0;
            for (Task t : tasks) {
                maxId = t.getId();
            }
            System.out.println("max id: " + maxId);
            task = new Task(maxId + 1, taskName, "pending");
        } else {
            task = new Task(1, taskName, "pending");
        }
        tasks.add(task);
        System.out.println("new task added: " + task);
    }

    public static List<Task> getTasks() {
        List<Task> tasks = new ArrayList<>();
        tasks.add(new Task(1, "task1", "pending"));
        tasks.add(new Task(2, "task2", "pending"));
        tasks.add(new Task(3, "task3", "pending"));
        tasks.add(new Task(4, "task3", "pending"));
        return tasks;
    }

    public static void updateTask(int taskId, String taskName) {
        List<Task> tasks = getTasks();
        for (Task task : tasks) {
            if (task.getId() == taskId) {
                task.setTask(taskName);
                tasks.add(task);
                System.out.println("task updated successfully: " + task);
                break;
            }
        }
    }

    public static void deleteTask(int taskId) {
        List<Task> tasks = getTasks();
        for (Task task : tasks) {
            if (task.getId() == taskId) {
                tasks.remove(task);
                System.out.println("task removed successfully: " + tasks);
                break;
            }
        }
    }

    public static void markInprogress(int taskId) {
        List<Task> tasks = getTasks();
        for (Task task : tasks) {
            if (task.getId() == taskId) {
                task.setStatus("in-progress");
                tasks.add(task);
                System.out.println("task set to in-progress successfully: " + task);
                break;
            }
        }
    }

    public static void markCompleted(int taskId) {
        List<Task> tasks = getTasks();
        for (Task task : tasks) {
            if (task.getId() == taskId) {
                task.setStatus("done");
                tasks.add(task);
                System.out.println("task completed successfully: " + task);
                break;
            }
        }
    }

    public static List<Task> filterIncompleteTasks() {
        List<Task> tasks = getTasks();
        List<Task> filteredList = new ArrayList<>();
        if (!tasks.isEmpty()) {
            filteredList = tasks.stream()
              .filter(task -> !task.getStatus().equals("done"))
              .collect(Collectors.toList());
        }
        return filteredList;
    }

    public static List<Task> filterCompletedTasks() {
        List<Task> tasks = getTasks();
        List<Task> filteredList = new ArrayList<>();
        if (!tasks.isEmpty()) {
            filteredList = tasks.stream()
              .filter(task -> task.getStatus().equals("done"))
              .collect(Collectors.toList());
        }
        return filteredList;
    }
}
