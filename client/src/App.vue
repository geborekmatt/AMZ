<template>
  <div>
    <div>
      <MenuBar  :model="items" />
    </div>
    <div>
      <RouterView />
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      items: [
        {
          label: "Home",
          icon: "pi pi-home",
          command: () => {
              this.$router.push('/');
          }
        },
        {
          label: "HW",
          icon: "pi pi-save",
          visible: true,
          command: () => {
                        this.$router.push('/hw');
                    }
        },
        {
          label: "Brands",
          icon: "pi pi-save",
          visible: true,
          command: () => {
                        this.$router.push('/brands');
                    }
        },
      ],
    };
  },
  methods: {
  },
};
</script>
<style scoped> 
</style>
