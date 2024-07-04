import {
  createRouter,
  createWebHistory,
  createMemoryHistory,
} from "vue-router";
import axios from "axios";

const baseUrl = import.meta.env.BASE_URL;
const history = import.meta.env.SSR
  ? createMemoryHistory(baseUrl)
  : createWebHistory(baseUrl);

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("../views/MainPage.vue"),
  },

  {
    path: "/cabinet",
    name: "cabinet",
    component: () => import("../views/UserProfile.vue"),
    meta: {
      requiresAuth: true,
      active: true,
      profile: true,
    },
  },
  /*
  {
    path: "/userlist",
    name: "userlist",
    component: () => import("../views/Userlist.vue"),
    meta: {
      requiresAuth: true,
      active: true,
      admin: true,
    },
  },
  {
    path: "/rolelist",
    name: "rolelist",
    component: () => import("../views/RoleList.vue"),
    meta: {
      requiresAuth: true,
      active: true,
      admin: true,
    },
  },
  */
  {
    path: "/register",
    name: "registerpage",
    component: () => import("../views/RegisterPage.vue"),
  },
  {
    path: "/login",
    name: "loginpage",
    component: () => import("../views/LoginPage.vue"),
  },

  {
    path: "/reset_password",
    name: "reset_password",
    component: () => import("../views/ChangePassword.vue"),
    meta: {
      requiresAuth: true,
      active: true,
    },
  },
  {
    path: "/notauth",
    name: "Notauth",
    component: () => import("../views/authComponents/NotAuthorized.vue"),
  },
  {
    path: "/notactive",
    name: "Notactive",
    component: () => import("../views/authComponents/NotActive.vue"),
  },
  {
    path: "/:notFound",
    name: "pagenotfound",
    component: () => import("../views/PageNotFound.vue"),
  },
  {
    path: "/script",
    name: "script",
    component: () => import("../views/Script.vue"),
  },
];

function getCookie(cname) {
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

//console.log(getCookie('jwt'))

let jwt = getCookie('jwt');

const router = createRouter({
  history,
  routes,
});

let base_backend_url = "http://localhost:8000/";
let access_origin = "*"

if(import.meta.env.VITE_PROJECT_MODE === "production") {
  base_backend_url = "http://79.174.80.207:8000/";
  access_origin = "http://clio.ws"
}

//let base_backend_url = "http://localhost:8000/";
//let base_backend_url = "http://79.174.80.207:8000/";

//let access_origin = "*"
//let access_origin = "http://clio.ws"

router.beforeEach((to, from, next) => {
  let user = "";
  let role = {};
  jwt = getCookie('jwt')
  axios
    .get(base_backend_url + "user", {
      headers: {
        Authorization: jwt,
        "Access-Control-Allow-Credentials": true,
        "Access-Control-Allow-Origin": access_origin,
      },
      //withCredentials: true,
    })
    .then((response) => {
      console.log("что-то", response);
      user = response.data.user;
      role = response.data.role;
      console.log(to.matched.some((record) => record.meta.requiresAuth))
      if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (
          user == null ||
          user == undefined ||
          user.username === null ||
          user.username === undefined
        ) {
          console.log(1);
          next({
            path: "/login",
            params: { nextUrl: to.fullPath },
          });
        } else {
          if (to.matched.some((record) => record.meta.active)) {
            if (user.active == true) {
              console.log(2);

              if (to.matched.some((record) => record.meta.admin)) {
                if (role.admin === true) {
                  next();
                } else {
                  console.log(111, "dddd");
                  next({ path: "/notFound" });
                }
              } 
              if(to.matched.some((record) => record.meta.profile)) {
                if (role.profile === true) {
                  next();
                } else {
                  next({ path: "/notFound" });
                }
              }
              //else {
                //next();
              //}
              next();
            } else {
              console.log(3);
              next({ name: "Notactive" });
            }
          } else {
            console.log(4);
            next();
          }
        }
      } else {
        console.log(5, 1, 2, 3);
        next();
      }
    });
});

export default router;
