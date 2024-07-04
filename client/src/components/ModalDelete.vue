<template>
  <div class="modal fade " :id="`exampleModalDelete` + object" tabindex="-1" aria-labelledby="exampleModalDeleteLabel"
    aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalDeleteLabel">Вы уверены?</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" @Click="Cancel" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          Вы действительно хотите удалить {{objectType}} "<span v-if="objectToDelete.name !== undefined">{{ objectToDelete.name }}</span>
          <span v-else>{{ objectToDelete.username }}</span>"?
        </div>
        <div class="modal-footer mx-auto">
          <button type="button" class="btn btn-secondary" @click="Cancel" data-bs-dismiss="modal">Отмена</button>
          <button type="button" class="btn btn-danger" @click="Delete" data-bs-dismiss="modal">Удалить</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    object: {
      type: String,
      required: true,
    },
    objectType: {
      type: String,
      required: true,
    },
    objectToDelete: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      test: '1',
    }
  },
  methods: {
    Cancel() {
      this.$emit(`Cancel`)
    },
    Delete() {
      this.$emit(`Delete`, this.objectToDelete)
    }
  }
}
</script>

<style></style>