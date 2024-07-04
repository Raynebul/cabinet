<script setup>
import axios from "axios";
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="col" v-for="i in trainercourses.length" :key="i">
    <div class="card shadow-sm" style="height: 15rem">
      <div class="card-body">
        <div class="d-flex">
          <div style="height: 60px; width: 60px; background-color: grey"></div>
          <div class="ms-2">
            <div class="text-muted" style="font-size: 1rem">
              {{ trainercourses[i - 1].name }}
            </div>
            <div class="text-muted mt-auto">
              {{ trainercourses[i - 1].author }}
            </div>
          </div>
        </div>
        <div class="card-text text-muted">
          0/{{ trainercourses[i - 1].number_of_tasks }}
        </div>
        <div class="card-text text-muted" style="margin-top: auto">
          Сложность: {{ trainercourses[i - 1].difficulty }}
        </div>
        <div class="d-flex" style="margin-top: 50px">
          <!--
          <RouterLink
            :to="`/createtrainercourse/` + i"
            class="btn btn-sm btn-secondary"
            >Редактировать</RouterLink
          >-->
          <button
            style="margin-top: auto"
            class="btn"
            data-bs-toggle="modal"
            :data-bs-target="`#exampleCourseModal` + trainercourses[i - 1].id"
          >
            ...
          </button>
          <a
            type="button"
            :href="`/trainercourse/` + trainercourses[i - 1].id"
            class="btn btn-sm btn-primary"
            style="margin-left: auto; margin-top: 5px"
          >
            Начать обучение
          </a>
        </div>
      </div>
    </div>
  </div>

  <div v-for="i in trainercourses.length" :key="i">
    <div
      class="modal fade"
      :id="`exampleCourseModal` + i"
      tabindex="-1"
      aria-labelledby="exampleCourseModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <div>
              <h5 class="modal-title" id="exampleCourseModalLabel">
                {{ trainercourses[i - 1].name }}
              </h5>
              <div class="text-muted text-start" style="font-size: 0.8rem">
                Автор: {{ trainercourses[i - 1].author }}
              </div>
            </div>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>

          <div class="modal-body">
            <h6 class="text-muted">Описание</h6>
            <div>{{ trainercourses[i - 1].description }}</div>
          </div>
          <div class="modal-footer">
            <!--
            <div class="btn btn-danger btn-sm" style="margin-right: auto">
              Удалить
            </div>-->
            <div
              class="btn-group btn-group-sm"
              role="group"
              aria-label="Basic example"
            >
              <a
                type="button"
                class="btn btn-secondary"
                :href="`/createtrainercourse/` + trainercourses[i - 1].id"
              >
                Редактировать
              </a>
              <a
                type="button"
                :href="`/trainercourse/` + trainercourses[i - 1].id"
                class="btn btn-primary"
              >
                Запустить
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    trainercourses: {
      type: Object,
      required: true,
      default: () => {},
    },
  },
  data(props) {
    //let new_trainers = props.trainers;
    //console.log("тренажёры -", new_trainers);
    //  for (let i = 0; i < new_trainers.length; i++) {
    //console.log(new_trainers[i].dataUI)
    //  new_trainers[i].dataUI = JSON.parse(new_trainers[i].dataUI);
    // }
    //console.log(Trainer.name);
    //let status = "Студент";
    //let telephone = "7 (910) 540-45-22"
    // return {
    // new_trainers,
    // edit: false,
    // };
  },
  /*
  methods: {
    RemoveModalConstructing(i) {
      //let id = "exampleModal" + String(id);
      //console.log("closed");
      let route = this.$router.resolve({
        name: `updaterainercourse`,
        params: {
          id: this.trainercourses[i].id,
        },
      });
      window.open(route.href);

      //this.$router.push(`/constructor/` + this.metadatas[i].id)
      //this.$bvModal.hide(id)
    },
    RemoveModalTrainer(i) {
      //let id = "exampleModal" + String(id);
      //console.log("closed");
      let route = this.$router.resolve({
        name: `trainercourse`,
        params: {
          id: this.trainercourses[i].id,
        },
      });
      window.open(route.href);

      //this.$router.push(`/constructor/` + this.metadatas[i].id)
      //this.$bvModal.hide(id)
    },
    GoToConstructing(i) {
      this.$router.push(`/createtrainercourse/` + this.trainercourses[i].id);
    },
    GoToTrainer(i) {
      this.$router.push(`/trainercourse/` + this.trainercourses[i].id);
    },
  }, */
};
</script>
