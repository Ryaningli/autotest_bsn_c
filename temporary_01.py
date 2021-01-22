n = 'app_test_600001'


def get_name(number):
      app_name = []
      with open('./data/app_create_and_release_app_name.txt', 'r') as f:
            current_name = f.readline()

      for i in range(number):
            name = 'app_test_' + str(int(current_name[-6:]) + i + 1)
            app_name.append((name,))

      with open('./data/app_create_and_release_app_name.txt', 'w') as f:
            f.write(app_name[-1][0])

      return app_name


print((get_name(10)))