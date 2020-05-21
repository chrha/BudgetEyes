<template>
    <div id="stock-log">
        <v-container id="log-container">
            <v-row class="mb-5">
                <v-col>
                  <v-btn id= "followButton" 
                  v-on:click="onFollow()"> {{followButton}}</v-btn>
                </v-col>

            </v-row>

            <v-row>
                <v-col >
                    <v-overflow-btn
                        class="my-2"
                        v-model="value"
                        @change="onChange(value)"
                        :items="followed_dropdown"
                        label="Followed Stocks"
                        editable
                        item-value="text"
                    ></v-overflow-btn>           
                </v-col>
            </v-row>
            <v-row>
            </v-row>
        </v-container>
    </div>
</template>


<script>
export default {
  name: 'StockLog',
  data() { 
    return {
      followed_dropdown: 
          [
            { text: 'stock1' },
            { text: 'stock2' },
            { text: 'stock4' },
          ],
      bought_dropdown: 
          [
            { text: 'bought1' },
            { text: 'bought2' },
            { text: 'bought3' },
          ],
      available_stocks:
        [
          { text: 'stock1' },
          { text: 'stock2' },
          { text: 'stock3' },
          { text: 'stock4' },
          { text: 'stock5' },
        ],
      value: '',
      disp_stock: '',
      followButton: 'Follow',
    };
  },
  mounted() {
    this.$root.$on('msg_from_stockcomp', (shownStock) => {
      this.disp_stock = shownStock;
      console.log('madlad: '.concat(this.disp_stock));
      Object.keys(this.followed_dropdown).forEach((index) => {
        console.log(index);
        if (this.followed_dropdown[index] === shownStock) {
          this.followButton = 'Unfollow';
        } else this.followButton = 'Follow';
      });
      console.log('loop');
    });
    console.log('outside msg rec');
  },
  methods: {
    onChange(value) {
      console.log(value);
      this.followButton = 'Unfollow';
      this.$root.$emit('msg_from_stocklog', value);
    },
    onFollow() {
      let key = 0;
      Object.keys(this.followed_dropdown).forEach((i) => {
        console.log('on followloop'.concat(this.followed_dropdown[i].text).concat(this.disp_stock));
        if (this.followed_dropdown[i].text === this.disp_stock) {
          this.followButton = 'Unfollow';
          key = i;
          console.log(this.followed_dropdown[i].concat(': ').concat(i));
        }
      }); 
      if (this.followButton === 'Follow') {
        this.followed_dropdown.push({ text: this.disp_stock });
        this.value = this.disp_stock;
        this.followButton = 'Unfollow';
      } else if (this.followButton === 'Unfollow') {
        this.followed_dropdown.splice(key, 1);
        this.followButton = 'Follow';
      }
    },
  },

};
</script>



<style scoped>
    #followButton{
        background-color: #C7F0DB;
        color: #000000;    
    }
     #buyButton{
        background-color: #C7F0DB;
        color: #000000;    
    }
     #unfollowButton{
        background-color: #C7F0DB;
        color: #000000;    
    }
</style>
