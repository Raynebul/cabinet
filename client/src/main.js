import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import "./scss/styles.scss";
import * as bootstrap from "bootstrap";
import "bootstrap-icons/font/bootstrap-icons.css";

let base_url = "http://localhost:8000";
let base_frontend_url =  "http://localhost:5000";
let base_backend_url =  "http://localhost:8000";
let clio =  ["http://clio.ws", "http://79.174.80.207"];
let sim_frontend_url =  "http://localhost:5173";
let problem_frontend_url =  "http://localhost:5173";
let question_frontend_url =  "http://localhost:5173";
let sim_backend_url =  "http://localhost:3000";
let access_origin =  "*";
let domain_clio =  "";

if(import.meta.env.VITE_PROJECT_MODE === "production") {
  base_url = "http://79.174.80.207:8000";  
  base_frontend_url = "http://clio.ws";
  base_backend_url = "http://79.174.80.207:8000";
  sim_frontend_url = "http://clio.ws/simulator";
  problem_frontend_url = "http://clio.ws/problem";
  question_frontend_url = "http://clio.ws/question";
  sim_backend_url = "http://79.174.80.207:3000";    
  clio = ["http://clio.ws", "http://79.174.80.207"];   
  access_origin = "http://clio.ws";       
  domain_clio = "domain=clio.ws";
}


var myGlobalVariable = {
    data() {
      return {
        base_url: base_url,
        base_frontend_url: base_frontend_url,
        base_backend_url: base_backend_url,
        sim_frontend_url: sim_frontend_url,
        problem_frontend_url: problem_frontend_url,
        question_frontend_url: question_frontend_url,
        sim_backend_url: sim_backend_url,
        clio: clio,
        access_origin: access_origin,
        domain_clio: domain_clio,
      };
    },
  };

  const app = createApp(App);
  app.use(router);
  app.mixin(myGlobalVariable);
  
  app.mount("#app");
