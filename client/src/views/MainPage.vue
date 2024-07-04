<template>
  <div class="wrapper">
    <!--min-vh-100 -->
    <section class="align-middle">
      <div class="grid-wrapper mainpage-text">
        <div class="grid">
          <div class="col will-slide-in-up slide-in-up-group">
            <!---->
            <h1 class="text-center animated-text  display-2"><strong style="font-family: 'Inter', sans-serif; font-weight: 700;"><span class="main-text">Учебная платформа</span>
                <span class="clio px-3 py-1">Клио</span></strong>
            </h1>
            <!--pt-4-->
            <h5 class="text-center text-muted code " style="margin-left: auto; margin-right: auto">
              Учебная платформа Клио позволяет генерировать вопросы и задачи, создавать тренажеры и учебные курсы
            </h5>
          </div>

        </div>
      </div>
    </section>
    <!--
    <section class="min-vh-100">
      <div class=" grid-wrapper mainpage-text">
        <div class="grid">
          <div class="col will-slide-in-up slide-in-up-group">
            <h1 class="text-center animated-text text-for-constructor"><b>КОНСТРУКТОР ТРЕНАЖЁРОВ</b></h1>
            <div class="container text-center">
              <div class="row pt-5">
                <div class="col">
                  <img src="../assets/sim_page.png" class="img-fluid" alt="...">
                </div>
                <div class="col">
                  <div class="d-flex flex-column text-start list-text">
                    <div class="py-3"><i class="bi bi-check2-circle"></i>Создайте тренажер любой
                      сложности в
                      конструкторе</div>
                    <div class="py-3"><i class="bi bi-check2-circle"></i> Не нужно писать <span
                        class="list-english-text">HTML
                      </span> и <span class="list-english-text">CSS</span>
                      для UI
                      конструктора</div>
                    <div class="py-3"><i class="bi bi-check2-circle"></i>Совмещено с библиотекой
                      <span class="list-english-text">Plotly.js</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>
    <section class="min-vh-100">
      <div class=" grid-wrapper mainpage-text">
        <div class="grid">
          <div class="col">
            <h1 class="text-center animated-text text-for-constructor"><b>КОНСТРУКТОР ВОПРОСОВ</b></h1>
            <div class="container text-center">
              <div class="row pt-5">
                <div class="col">
                  <div class="d-flex flex-column text-start list-text">
                    <div class="py-3"><i class="bi bi-check2-circle"></i> Создайте тренажер любой
                      сложности в
                      конструкторе</div>
                    <div class="py-3"><i class="bi bi-check2-circle"></i> Не нужно писать HTML и CSS
                      для UI
                      конструктора</div>
                    <div class="py-3"><i class="bi bi-check2-circle"></i>Совмещено с библиотекой
                      Plotly.js</div>
                  </div>
                </div>
                <div class="col">
                  Column
                </div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>
    <section class="min-vh-100">
      <div class=" grid-wrapper mainpage-text">
        <div class="grid">
          <div class="col">
            <h1 class="text-center animated-text text-for-constructor"><b>КОНСТРУКТОР ЗАДАЧ</b></h1>
            <div class="container text-center">
              <div class="row pt-5">
                <div class="col">
                  Column
                </div>
                <div class="col">
                  <div class="d-flex flex-column text-start list-text">
                    <div class="py-3"><i class="bi bi-check2-circle"></i> Создайте тренажер любой
                      сложности в
                      конструкторе</div>
                    <div class="py-3"><i class="bi bi-check2-circle"></i> Не нужно писать HTML и CSS
                      для UI
                      конструктора</div>
                    <div class="py-3"><i class="bi bi-check2-circle"></i>Совмещено с библиотекой
                      Plotly.js</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>-->

  </div>
</template>
  
<style>
/*
  h1 {
    font-size: 72px;
    background: -webkit-linear-gradient(#eee, #333);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  */
.wrapper {
 /* background-color: #f7fbff; */
}

.code {
  font-family: "Lucida Console", "Courier New", monospace;
  animation: textmove 1s;
  animation: fadein 1s;

}

.clio {
  background-image: -webkit-linear-gradient(#02ffe2, #0f35cd);
  /*-webkit-background-clip: text;*/
  /*-webkit-text-fill-color: transparent;*/
  margin-left: 15px;
  color: white
}

.grid-wrapper {
  /*padding: 0 24px; */
  max-width: 1000px;
  margin: 0 auto;
  padding-top: 15%;
  padding-bottom: 15%;
}

.main-text {
  /*background: linear-gradient(to right, #02ffe2, #0f35cd);*/
  background: -webkit-linear-gradient(#02ffe2, #0f35cd);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  /*background-image: linear-gradient(45deg, #02ffe2, #0f35cd);
  background-size: 100%;
  background-repeat: repeat;*/
}

.will-slide-in-up {
  transition-property: opacity;
  transition-duration: 0.7s;
  transition-timing-function: ease;
  transition-delay: 0s
}

.will-slide-in-up {
  opacity: 0
}

.slide-in-up-group {
  opacity: 1
}

.text-for-constructor {
  color: #484e4d;
  font-family: "Lucida Console", "Courier New", monospace;
}

.animated-text {
  position: relative;
 /* font-family: 'Inter', sans-serif; */
  animation: textmove 1s;
  animation: fadein 1s;
}

.list-text {
  font-family: 'Quicksand', sans-serif
}

.list-text .py-3 .bi {
  padding-right: 1rem;
  font-size: 1.25rem;
  color: #0674f2;
}

.list-english-text {
  color: #07b5e0;
}

@keyframes textmove {
  from {
    right: -40px;
  }

  to {
    right: 0px;
  }
}


@keyframes fadein {
  from {
    /*  top: -200px; */
    opacity: 0;
  }

  to {
    /*   top: 0px; */
    opacity: 1;
  }
}

.carousel-caption {
  top: 50%;
  transform: translateY(-50%);
  bottom: initial;
}

.item {
  -webkit-transform-style: preserve-3d;
  -moz-transform-style: preserve-3d;
  transform-style: preserve-3d;
}
</style>
  
<script setup>
import { RouterLink } from "vue-router";
import axios from "axios";
</script>
  
<script>
export default {
  data() {
    return {
      username: "",
      info: null,
      IsAuth: false,
    };
  },
  /*
  async created() {
    const response = await axios.get(this.base_url + "user");
    console.log(response);
  }, */
};
</script>
  