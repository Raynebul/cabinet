<script setup>
import { RouterLink } from "vue-router";
import axios from "axios";
import Toast from "./Toast.vue";

import MetadataEdit from "./../../components/MetadataEdit.vue"
import ModalDelete from "./../../components/ModalDelete.vue"
</script>

<template>
  <div class="col" v-for="i in materials.length" :key="i">
    <div class="card shadow-sm" style="min-height: 14rem; max-height: 14rem;">
      <div class="card-body border-start border-2 ms-2" :style="BorderStyleType(materials[i - 1].metadata_.type)">
        <div class="d-flex ">
          <div v-if="materials[i - 1].metadata_.cover != undefined && materials[i - 1].metadata_.cover != ``">
            <img style="height: 45px; width: 45px;" :src="materials[i - 1].metadata_.cover" class="img-fluid"
              alt="..." />
          </div>
          <div v-else style="height: 45px; width: 45px; background-color: grey"></div>
          <div style="margin-top: -5px">
            <div v-if="isNameLong[i-1] === 2"  class="text-muted mt-auto ms-2 long-name" :id="`Material` + String(i)" :ref="`material` + String(i)"
              :style="`font-size: 1rem; max-width: 10rem;` + styles[i - 1]" data-bs-toggle="tooltip" data-bs-placement="top" :title="materials[i - 1].metadata_.name">
              {{ names[i - 1] }}
            </div>
            <div v-else class="text-muted mt-auto ms-2 long-name"  :id="`Material` + String(i)" :ref="`material` + String(i)"
              :style="`font-size: 1rem; max-width: 10rem;` + styles[i - 1]" >
              {{ materials[i - 1].metadata_.name }}
            </div>
            <div class="text-muted mt-auto ms-2" style="font-size: 0.8rem">
              Тип: {{ materials[i - 1].metadata_.type }}
            </div>
            <!--
            <div class="text-muted mt-auto ms-2" style="font-size: 0.8rem">
              Автор: {{ materials[i - 1].metadata_.author }}
            </div>-->
          </div>
        </div>
        <div class="card-text text-muted ">
          Автор: {{ materials[i - 1].metadata_.author }}
        </div>
        <div class="card-text text-muted ">
          Статус: {{ materials[i - 1].metadata_.status }}
        </div>
        <div class="card-text text-muted" style="margin-top: auto;">
          Создан: {{ materials[i - 1].metadata_.created }}
        </div>
        <!--
        <div @click="GetData()" class="btn btn-success">___</div>-->
        <!--style="margin-top: 50px;"-->
        <!--20,  39.2, margin-top-->
        <div class="d-flex" v-if="isNameLong[i-1] !== 0" style="margin-top: 20px">
          <div style="margin-top: 0px !important; margin-left: -10px !important; margin-bottom: 0px !important;"
            class="dropdown ms-auto m-2">
            <button class="btn console-text " type="button" id="dropdownMenuButton2"
              data-bs-toggle="dropdown" aria-expanded="false">
              ...
            </button>
            <ul class="dropdown-menu dropdown-menu-dark" style="border-radius: 0;"
              aria-labelledby="dropdownMenuButton2">
              <li><a class="dropdown-item my-1 dropdown-item-edit" href="#" data-bs-toggle="modal"
                  :data-bs-target="`#exampleModal` + i">Редактировать метаданные</a></li>
              <li><a class="dropdown-item my-1 dropdown-item-edit" :href="sim_frontend_url + `/edit/` + materials[i - 1].metadata_.id">Редактировать тренажёр</a></li>
              <li><a class="dropdown-item my-1 dropdown-item-delete" data-bs-toggle="modal"
                  data-bs-target="#exampleModalDeleteTrainer" @click="ChooseObjectForDelete(materials[i - 1])"
                  href="#">Удалить</a></li>
            </ul>
          </div>
          <a v-if="materials[i - 1].metadata_.type === `Тренажёр`"
            :href="sim_frontend_url + `/run/` + materials[i - 1].metadata_.id" type="button"
            class="btn btn-secondary btn-sm" style="margin-left: auto; margin-top: 5px">Запустить</a>
          <a v-if="materials[i - 1].metadata_.type === `Задача`" :href="problem_frontend_url + `/run/`" type="button" class="btn btn-secondary btn-sm"
            style="margin-left: auto; margin-top: 5px">Запустить</a>
          <a v-if="materials[i - 1].metadata_.type === `Вопрос`" :href="question_frontend_url + `/run/`" type="button" class="btn btn-secondary btn-sm"
            style="margin-left: auto; margin-top: 5px">Запустить</a>
        </div>
        <div class="d-flex" v-else style="margin-top: 39.2px">
          <div style="margin-top: 0px !important; margin-left: -10px !important; margin-bottom: 0px !important;"
            class="dropdown ms-auto m-2">
            <button class="btn console-text " type="button" id="dropdownMenuButton2"
              data-bs-toggle="dropdown" aria-expanded="false">
              ...
            </button>
            <ul class="dropdown-menu dropdown-menu-dark" style="border-radius: 0;"
              aria-labelledby="dropdownMenuButton2">
              <li><a class="dropdown-item my-1 dropdown-item-edit" href="#" data-bs-toggle="modal"
                  :data-bs-target="`#exampleModal` + i">Редактировать метаданные</a></li>
              <li><a class="dropdown-item my-1 dropdown-item-edit" :href="sim_frontend_url + `/edit/` + materials[i - 1].metadata_.id">Редактировать тренажёр</a></li>
              <li><a class="dropdown-item my-1 dropdown-item-delete" data-bs-toggle="modal"
                  data-bs-target="#exampleModalDeleteTrainer" @click="ChooseObjectForDelete(materials[i - 1])"
                  href="#">Удалить</a></li>
            </ul>
          </div>
          <a v-if="materials[i - 1].metadata_.type === `Тренажёр`"
            :href="sim_frontend_url + `/run/` + materials[i - 1].metadata_.id" type="button"
            class="btn btn-secondary btn-sm" style="margin-left: auto; margin-top: 5px">Запустить</a>
          <a v-if="materials[i - 1].metadata_.type === `Задача`" :href="problem_frontend_url + `/run/`" type="button" class="btn btn-secondary btn-sm"
            style="margin-left: auto; margin-top: 5px">Запустить</a>
          <a v-if="materials[i - 1].metadata_.type === `Вопрос`" :href="question_frontend_url + `/run/`" type="button" class="btn btn-secondary btn-sm"
            style="margin-left: auto; margin-top: 5px">Запустить</a>
        </div>
      </div>
    </div>
  </div>
  <ModalDelete @Delete="Delete" @Cancel="Cancel" :object="`Trainer`" :objectType="`материал`"
    :objectToDelete="objectToDelete"></ModalDelete>
  <MetadataEdit @saveMetadata="SaveMetadata" v-for="i in materials.length" :key="i"
    :Metadata="materials[i - 1].metadata_" :id="materials[i - 1].id" :index="i" :user="user"></MetadataEdit>
  <Toast :notificationText="toastString" :color="`green`" :hideToast="hideToast" @hideToast="HideToast()"></Toast>
</template>

<script>
export default {
  props: {
    user: {
      type: Object,
      required: true,
      default: () => { },
    },
    materials: {
      type: Object,
      required: true,
      default: () => { },
    },
    toastString: {
      type: String,
      required: true,
    },
    isEditing: {
      type: Object,
      default: () => { },
    },
    reload: {
      type: Number,
    },
    hideToast: Boolean,
  },
  data(props) {
    //let new_trainers = props.trainers;
    let length_of_names = [];
    let names = [];
    let styles = [];
    let isNameLong = [];
    for (let i = 0; i < props.materials.length; i++) {
      length_of_names.push(props.materials[i].name.length);
      styles.push(" ");
      names.push(props.materials[i].name);
      isNameLong.push(0);
    }
    return {
      edit: false,
      objectToDelete: {},
      length_of_names,
      styles,
      names,
      isNameLong,
    };
  },
  watch: {
    reload: {
      handler(newVal, oldVal) {
        //console.log("sososo", this.names)
        if(this.names.length === 0)
        {
          this.names = [];
          this.isNameLong = [];
          for (let i = 0; i < this.materials.length; i++) {
              //console.log(i, "проверка")
             this.names.push(this.materials[i].name);
             this.isNameLong.push(0);
           }
        }
        this.SetNewName()
      },
      deep: true,
    },
  },
  mounted: function () { //

  },
  methods: {
    BorderStyleType(type) {
      switch (type) {
        case "Тренажёр": {
          return "border-color: #0dffe3 !important;"
        }
        case "Задача": {
          return "border-color : #0d9aff!important; "
        }
        case "Вопрос": {
          return "border-color: #b90ff7 !important;  "
        }
        default: {
          return "border-color: #878787 !important;"
        }
      }
    },
    ButtonStyleType(type) {
      switch (type) {
        case "Тренажёр": {
          return "border-color: #0dffe3 !important;"
        }
        case "Задача": {
          return "border-color : #0d9aff!important; "
        }
        case "Вопрос": {
          return "border-color: #b90ff7 !important;  "
        }
        default: {
          return "border-color: #878787 !important;"
        }
      }
    },
    SaveMetadata(metadata, name, index) {
      this.$emit(`saveMetadata`, metadata, name, index)
    },
    HideToast() {
      this.$emit(`HideToast`);
      //this.hideToast = true;
    },
    ChooseObjectForDelete(object) {
      this.objectToDelete = object;
    },
    Cancel() {
      this.objectToDelete = {};
    },
    Delete(material) {
      console.log("Удалён", material)
      this.$emit('deleteMaterial', material)
    },
    LengthOfName(name, id) {
      if (this.$refs[`material` + String(id)] == undefined) {
        return name;
      }
      else {
        return name;
      }
    },
    GetData() {
      //console.log(this.$refs["material1"].clientHeight)
      //let width=this.$refs["material1"].clientHeight;
      //let height=this.$refs["material1"].clientHeight;
      //console.log(width+", "+height)

      console.log(document.getElementById("Material7").clientHeight);
      console.log()
    },
    /*
    SetNewStyle() {
      for (let i = 0; i < this.materials.length; i++) {
        let height = document.getElementById("Material" + String(i + 1)).clientHeight;
        console.log("веревка", height);
        if (height > 24) {
          this.styles[i] = "height: 24px; "
        }
      }
    }, */
    SetNewName() {
      for (let i = 0; i < this.materials.length; i++) {
        let height = document.getElementById("Material" + String(i + 1)).clientHeight;
        if (height > 24 && height <= 48) {
          this.isNameLong[i] = 1;
        }
        let lastIndexChar = 40;
        let minus = 5;
        if (height > 48) {
          lastIndexChar -= minus;
          this.isNameLong[i] = 2;
        } 
      }
    }
  }
};
</script>

<style>
.console-text {
  font-family: "Lucida Console", "Courier New", monospace;
  font-size: 0.9rem;
}

.dropdown-item-delete:hover {
  color: red
}

.dropdown-item-edit:hover {
  color: aqua
}

.long-name {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
