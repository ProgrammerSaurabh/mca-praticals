#### Implement queue using circular queue

##### To run the code

`g++ circularQueueArray.cpp  -o circularQueueArray && ./circularQueueArray`

##### Code

```
//circularQueueArray.cpp

#include <iostream>

using namespace std;

#define MAX 5

class Queue
{
private:
    int queue[MAX];

    int front, rear;

public:
    Queue()
    {
        front = -1;
        rear = -1;

        for (int i = 0; i < MAX; i++)
        {
            queue[i] = -1;
        }
    }

    void enqueue()
    {
        if (isFull())
        {
            cout << "Queue overflow!!" << endl;

            return;
        }

        if (isEmpty())
        {
            front = 0;
            rear = -1;
        }

        int element;

        cout << "Enter data: ";

        cin >> element;

        rear = (rear + 1) % MAX;

        queue[rear] = element;
    }

    int dequeue()
    {
        if (isEmpty())
        {
            cout << "Queue is empty!!" << endl;

            return -1;
        }

        int del = queue[front];

        if (front == rear)
        {
            front = rear = -1;
        }
        else
        {
            front = (front + 1) % MAX;
        }

        cout << "Element " << del << " removed" << endl;

        return del;
    }

    void print()
    {
        if (isEmpty())
        {
            cout << "Queue is empty!!" << endl;

            return;
        }

        cout << "Queue elements are : ";

        int i = front;
        do
        {
            cout << queue[i] << " ";
            i = (i + 1) % MAX;
        } while (i != (rear + 1) % MAX);

        cout << endl;
    }

    bool isFull()
    {
        return (rear + 1) % MAX == front;
    }

    bool isEmpty()
    {
        return front == -1 && rear == -1;
    }

    void frontEl()
    {
        if (isEmpty())
        {
            cout << "Queue is empty!!" << endl;
            return;
        }

        cout << "Element at front is : " << queue[front] << endl;
    }

    void back()
    {
        if (isEmpty())
        {
            cout << "Queue is empty!!" << endl;
            return;
        }

        cout << "Element at back is : " << queue[rear] << endl;
    }
};

int main()
{
    Queue queue;

    int menu;

    while (1)
    {
        cout << "1. Enqueue" << endl;
        cout << "2. Dequeue" << endl;
        cout << "3. Print elements" << endl;
        cout << "4. Element at front" << endl;
        cout << "5. Element at back" << endl;
        cout << "6. Exit" << endl;
        cout << "Enter your choice: " << endl;

        cin >> menu;

        switch (menu)
        {
        case 1:
            queue.enqueue();
            break;

        case 2:
            queue.dequeue();
            break;

        case 3:
            queue.print();
            break;

        case 4:
            queue.frontEl();
            break;

        case 5:
            queue.back();
            break;

        default:
            exit(0);
            break;
        }
    }

    return 0;
}
```

##### Output

![01 output](./01.JPG)
![02 output](./02.JPG)
![03 output](./03.JPG)
