package main.java;

import java.util.Objects;

public class Task {

    private int id;

    private String task;

    private String status;

    public Task() {}

    public Task(int id, String task, String status) {
        this.id = id;
        this.task = task;
        this.status = status;
    }

    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }

    public String getTask() {
        return task;
    }
    public void setTask(String task) {
        this.task = task;
    }

    public String getStatus() {
        return status;
    }
    public void setStatus(String status) {
        this.status = status;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Task task1 = (Task) o;
        return id == task1.id && Objects.equals(task, task1.task) && Objects.equals(status, task1.status);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, task, status);
    }

    @Override
    public String toString() {
        return "{" +
          "id=" + id +
          ", task='" + task + '\'' +
          ", status='" + status + '\'' +
          '}';
    }
}
