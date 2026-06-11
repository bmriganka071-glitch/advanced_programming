    #include <stdio.h>
    #include <pthread.h>

    #define THREADS 4
    #define INCREMENTS 1000000

    // Shared global counter
    long long counter = 0;
    // Mutex variable
    pthread_mutex_t lock;

    // ==========================================
    // WITHOUT MUTEX (Race Condition)
    // ==========================================

    void *increment_without_mutex(void *arg)
    {
        for (long long i = 0; i < INCREMENTS; i++)
        {
            counter++;   // Unsafe critical section
        }

       
        return NULL;
    }





    // ==========================================
    // WITH MUTEX (Safe Synchronization)
    // ==========================================

    void *increment_with_mutex(void *arg)
    {
        for (long long i = 0; i < INCREMENTS; i++)
        {
            pthread_mutex_lock(&lock);

            counter++;   // Protected critical section

            pthread_mutex_unlock(&lock);
        }

      
        return NULL;
    }





    // ==========================================
    // RUN TEST FUNCTION
    // Creates threads and executes given function
    // ==========================================

    void run_test(void *(*func)(void *), const char *test_name)
    {
        pthread_t tid[THREADS];

        // Reset counter before test
        counter = 0;

        printf("\n====================================\n");
        printf("%s\n", test_name);
        printf("====================================\n");

        // Create threads
        for (int i = 0; i < THREADS; i++)
        {
            pthread_create(&tid[i], NULL, func, NULL);
        }

        // Wait for all threads
        for (int i = 0; i < THREADS; i++)
        {
            pthread_join(tid[i], NULL);
        }

        // Print results
        printf("Final Counter Value = %lld\n", counter);
        printf("Expected Value      = %lld\n",
            (long long)THREADS * INCREMENTS);
    }





    int main()
    {
        // Initialize mutex
        pthread_mutex_init(&lock, NULL);

        // Test without mutex
        run_test(increment_without_mutex,
                "WITHOUT MUTEX (Race Condition)");

        // Test with mutex
        run_test(increment_with_mutex,
                "WITH MUTEX (Synchronized)");

        // Destroy mutex
        pthread_mutex_destroy(&lock);

        return 0;
    }