# cabinet

## Личный кабинет для учебной платформы Клио

##### Ссылка: http://clio.ws/

### Инструкция по настройке nginx:

1. Скачать nginx на сервер с помощью команды:
   `sudo apt install nginx`
2. Зайти в папку `/etc/nginx/sites_enabled`
3. Открыть файл **default**
4. Вставить код из файла **nginx.conf** в файл **default** и сохранить изменения
5. Перезапустить Nginx командой `sudo service nginx restart`


### Инструкция как поставить проект cabinet и sim на сервер Linux

1. Выполнить команду `sudo apt-get update`
2. Для начала нужно скачать docker и docker compose
3. Скачать Docker: `curl -fsSL https://get.docker.com -o get-docker.sh` и `sudo sh get-docker.sh`
4. Скачать docker-compose `sudo apt-get install docker-compose-plugin`
5. Зайти в папку `/`, создать папку `clio` и зайти в неё.
6. Клонировать репозиторий `git clone https://git.etude.team/clio/cabinet.git` 
7. Клонировать репозиторий `git clone https://git.etude.team/nstu/sim.git`
   7.5. Перейдите к пункту с установкой и настройкой nginx (если еще не сделано)
8. Зайти в папку `/cabinet`
9. Зайти в `/client` в файл .env и выставить VITE_PROJECT_MODE = `production`
10. Собрать docker'ы командой `sudo docker compose build` (Linux) или `docker-compose build` (Windows)
11. Запустить докеры `sudo docker compose up -d` (Linux) или `docker-compose up -d` (Windows)
12. зайдите в `/`
13. Выполните следующие команды:

```
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo swapon --show

```

14. Зайти уже в папку `/clio/sim`
15. Зайти в `/VUE-proj` файл .env и выставить VITE_PROJECT_MODE = `production` и VITE_TOKEN_MODE = `token`
16. В vite.config.js в define выставить `_global: {}`,
17. Собрать docker'ы командой `sudo docker compose build`
18. Запустить докеры `sudo docker compose up -d` (Linux) или `docker-compose up -d` (Windows)
19. Так как БД у cabinet будет пустая, мы не сможем зайти в профиль. Поэтому, нужно будет зайти по адресу http://clio.ws/script, нажать на кнопку "Запустить скрипт", и БД будет заполнена пользователями, ролями и материалами. После этого можно будет авторизоваться.
20. Если будет нужно остановить работу докеров, то `sudo docker compose down` (Linux) или `docker-compose up down` (Windows)


## Инструкция по добавлении нового сервиса:

### Инструкция по настройке nginx:
1. Зайти в папку `/etc/nginx/sites_enabled`
2. Открыть файл **default**
3. Если нужно будет добавить возможность запускать `/problem` и `/question`, то добавьте следующий код:

```nginx
	location /question {
		proxy_pass http://localhost:{Ваш порт client-сервера};
		proxy_http_version 1.1;
		proxy_set_header Upgrade $http_upgrade;
		proxy_set_header Connection 'upgrade';
		proxy_set_header Host $host;
		proxy_cache_bypass $http_upgrade;
	}
```

4. В <font color="##218bff">vite.config.js</font> в <font color="#00ffff">defineConfig</font> вашего проекта нужно добавить строчку:
```javascript
base: '/question/'
```
5. Снова перезапускаем Nginx `sudo service nginx restart`


### Инструкция для работы с токенами во VUE:
1. Атрибут preview в <font color="##218bff">vite.config.js</font> должен быть следующий:

```javascript
preview: {
    port: {Ваш порт client-сервера},
    strictPort: true,
    host: true,
    origin: "http://0.0.0.0:{Ваш порт client-сервера}",
}
```

2. JWT-токен пользователя хранится как куки. Чтобы получить токен пользователя, нужно добавить:

```javascript
async created() {
    let jwt = this.getCookie('jwt'); // получение jwt-токена
    const response = await axios.get(this.base_backend_url + "/user", {
      headers: {
        Authorization: jwt,
        "Access-Control-Allow-Origin": this.access_origin,
        "Access-Control-Allow-Credentials": true,
      },
    });
    console.log(response.data.user)
    if (!(response.data.user["username"] === undefined || response.data.user["username"] == null)) {
      this.user = response.data.user;
      if (this.user == null) {
        this.user = undefined;
      }
    }
  },
```

в data():

```javascript
return {
  user: undefined,
  /* ... и остальные параметры */
};
```

и в methods добавьте:

```javascript
   // получение куки
    getCookie(cname) {
      var name = cname + "=";
      var ca = document.cookie.split(';');
      for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
          c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
          return c.substring(name.length, c.length);
        }
      }
      return "";
    }
```

Если нужно будет добавить выход, то добавьте следующие методы:

```javascript
    // выход пользователя
    LogOut() {
      this.eraseCookie('jwt');
      localStorage.removeItem("jwt");
      if (this.route.path == "/") {
        window.location.reload();
      } else {
        this.$router.push("/");
      }
    },
    // удаление куки
    eraseCookie(name) {
      document.cookie = name + '=' + ';' + ' expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/;';
      console.log(document.cookie)
    },
```

3. В main.js добавьте:

```javascript
// ссылки на проект
var myGlobalVariable = {
    data() {
      return {
        base_frontend_url: "http://clio.ws",
        base_backend_url: "http://79.174.80.207:8000",
        access_origin: "http://clio.ws",
      };
    },
  };
...
app.mixin(myGlobalVariable);
```

4. В index.js, в котором описаны все пути проекта, добавьте:

```javascript
function getCookie(cname) {
  var name = cname + "=";
  var ca = document.cookie.split(";");
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

let jwt = getCookie("jwt");
let base_backend_url = "http://79.174.80.207:8000/";
let access_origin = "http://clio.ws";

router.beforeEach((to, from, next) => {
  let user = {};
  let role = {};
  jwt = getCookie("jwt");
  axios
    .get(base_backend_url + "user", {
      headers: {
        Authorization: jwt,
        "Access-Control-Allow-Credentials": true,
        "Access-Control-Allow-Origin": access_origin,
      },
    })
    .then((response) => {
      user = response.data.user;
      role = response.data.role;
      //to.matched.some((record) => record.meta.requiresAuth проверяется для роутов, в которых нужна авторизация. Если авторизация нужна, то дял каждого роута прописать:
      /*
	      meta: 
		  {
      		requiresAuth: true,
    	  }, 
	  */
      if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (
          user == null ||
          user == undefined ||
          user.username === null ||
          user.username === undefined
        ) {
          next({
            path: "/login",
            params: { nextUrl: to.fullPath },
          });
        } else {
          /* ваш код ранее к роутере или: */
          /* next(); */
        }
      } else {
        next();
      }
    });
});
```


### Инструкция как добавить метаданные при создании проекта: 
1. Добавить следующие данные:
```javascript
return {
   id: "test",
   name: "Test",
   user: {}, // чтобы получить токен пользователя, воспользуйтесь инстуркцией как получить токен пользователя
}
```
2. Добавит функцию, которая получает метаданные:
```javascript
    CreateMetadata() {
      let date = new Date();
      date = date.toLocaleDateString("ru");
      let metadata_ = {
        id: this.id, // данный id (IDtext) -личный идентификатор вашего материала для того, чтобы зайти на его страницу в сlio.ws. Например, есть material типа тренажера c IDtext = tm, и перейти по нему можно clio.ws/simulator/run/tm
        name: this.name, // Имя материала вашего (тренажера, задачи, вопроса и т. д.)
        author: this.user.username, // Это токен пользователя, чтобы данные получить, перейдите к инстуркции, как получать токен пользователя
        description: "",
        cover: "",
        created: date, 
        status: "В разработке",
        type: "Тренажёр", // Может быть еще как Вопрос или Задача
      };
      axios({
        method: "post",
        url: this.base_backend_url + "/metadata",
        data: {
          IDtext: this.id,
          name: this.name,
          metadata_: JSON.stringify(metadata_),
        },
        headers: {
          "Access-Control-Allow-Origin": this.access_origin,
          "Access-Control-Allow-Credentials": true,
        },
        validateStatus: (status) => {
          return true; // I'm always returning true, you may want to do it depending on the status received
        },
      })
        .catch((error) => {})
        .then((response) => {
        });
      //this.$router.push(`/edit/${this.id}`);
    },
```

### Инструкция как получать метаданные
1. Чтобы получить метаданные, вставьте следующую функцию:
```javascript
    async get_Metadata() {
        axios({
          method: "get",
          url: this.base_backend_url + "/metadata/" + this.$route.params.id,
          headers: {
            "Access-Control-Allow-Origin": this.access_origin,
            "Access-Control-Allow-Credentials": true,
          },
          validateStatus: (status) => {
            return true; // I'm always returning true, you may want to do it depending on the status received
          },
        }).then((response) => {
          this.Metadata = JSON.parse(response.data.metadata);
          this.metadata_id = response.data.new_id;
        });
    },
```

### Инструкция как редактировать метаданные

1. Чтобы редактировать метаданные, необходимо в проект добавить элемент MetadataEdit.vue в свой проект (находится в папке client/src/components). Кроме того, нужно также добавить компонент Toast.vue (находится в папке client/src/views/userComponents)
2. Изменить id в компоненте MetadataEdit.vue с `"MetadataEdit + index"` на `"MetadataEdit"`
3. Добавить следующие данные:
```javascript
return {
  Metadata: {},
  user: {},
  metadata_id: 1,
  hideToast: true,
  toastString: "",
}
```


4. Добавить компонент в свой код:
```javascript
import MetadataEdit from "../components/MetadataEdit.vue";
```

```html
  <MetadataEdit
    :Metadata="Metadata"
    :user="user"
    :id="metadata_id"
    @saveMetadata="SaveMetadata"
  ></MetadataEdit>
  <!--user - токен пользователя, Metadata и metadata_id - смотрите инстуркцию, как получать метаданные -->
```

5. Добавить компонент Toast:
```javascript
import Toast from "./constructorItems/Toast.vue";
```

```html
        <Toast
          :notificationText="toastString"
          :color="`green`"
          :hideToast="hideToast"
          @hideToast="HideToast()"
        ></Toast>
```


Добавить функции в компонент, в котором находится компонент MetadataEdit и Toast
```javascript
    SaveMetadata(metadata, name) {
      for (let key in metadata) {
        this.Metadata[key] = metadata[key];
      }
      this.toastString = "Метаданные сохранены!";
      this.hideToast = false;
    },
    HideToast() {
      this.hideToast = true;
    },
```
6. Элемент открывается как модальное окно, поэтому если будет нужно добавить кнопку, открывающее модальное окно:

```html
<button
  class="btn btn-primary"
  data-bs-toggle="modal"
  data-bs-target="#MetadataEdit"
  >Редактировать метаданные</button
>
```
