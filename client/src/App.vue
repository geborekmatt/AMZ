<template>
  <div>
    <div>
      <MenuBar class="bg-primary" :model="items" />
    </div>
    <div>
      <RouterView />
    </div>
    <Toast />
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
          label: "Hopper",
          icon: "pi pi-funnel",
          visible: true,
          command: () => {
                        this.$router.push('/hopper');
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
