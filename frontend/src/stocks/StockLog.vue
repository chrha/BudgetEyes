<template>
    <div id="stock-log">
        <v-container id="log-container">
            <v-row class="mb-5">
                <v-col>
                  <v-btn id= "followButton" 
                  v-on:click="onFollow()"
                  :disabled="buttonDisabled"
                  absolute
                  left
                  width="410px"
                  > 
                    {{followButton}}
                  </v-btn>
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
                        item-text="name"
                        item-value="abbriev"
                        width="420px"
                    ></v-overflow-btn>           
                </v-col>
            </v-row>
            <v-row>
            </v-row>
        </v-container>
    </div>
</template>

<script>
import axiosInstance from '../ajax/client';


export default {
  name: 'StockLog',
  data() { 
    return {
      followed_dropdown: [],
      value: '',
      disp_stock: '',
      disp_stock_name: '',
      followButton: 'Follow',
      buttonDisabled: false,
    };
  },
  /**
   * After the component is mounted, StockLog listens to StockComponent
   * for update on the displayed stock, and updates follow button.
   */
  mounted() {
    axiosInstance.get('stocks/handle_stocks/', { headers: { Authorization: `Token ${this.$cookies.get('token')}` } })
      .then((response) => {
        this.followed_dropdown = response.data;
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.log(error);
      });
    this.$root.$on('msg_from_stockcomp', (shownStock) => {
      this.disp_stock = shownStock;
      
      let check = true;
      Object.keys(this.followed_dropdown).forEach((index) => {
        if (this.followed_dropdown[index].text === shownStock) {
          this.followButton = 'Unfollow';
          this.value = this.followed_dropdown[index].abbriev;
          check = false;
        }
      });
      if (check) {
        this.followButton = 'Follow';
        this.value = '';
      }
    });
    this.$root.$on('msg_from_stocksearch', (shownStock) => {
      [this.disp_stock_name, this.disp_stock] = shownStock;
      let check = true;
      Object.keys(this.followed_dropdown).forEach((index) => {
        if (this.followed_dropdown[index].text === shownStock) {
          this.followButton = 'Unfollow';
          this.value = this.followed_dropdown[index].text;
          check = false;
        }
      });
      if (check) {
        this.followButton = 'Follow';
        this.value = '';
      }
    });
  },
  methods: {
    /**
     * updates followbutton and dropdown display value, which is sent to StockComponent
     */
    onChange(value) {
      const data = this.followed_dropdown.find((element) => element.abbriev === value);
      this.followButton = 'Unfollow';
      this.disp_stock = data.abbriev;
      this.disp_stock_name = data.name;
      
      this.$root.$emit('msg_from_stocklog', data);
    },  
    /**
     * Iterates dropdown list items and updates button whether
     *  to be able to remove or add displayed item to the list.
     */
    onFollow() {
      let key = 0;
      this.buttonDisabled = true;
      
      Object.keys(this.followed_dropdown).forEach((i) => {
        if (this.followed_dropdown[i].abbriev === this.disp_stock) {
          this.followButton = 'Unfollow';
          key = i;
        } 
      });
      const data = { stock: this.disp_stock };
      
      axiosInstance.put('stocks/handle_stocks/', data, { headers: { Authorization: `Token ${this.$cookies.get('token')}` } })
        .then(() => {
          if (this.followButton === 'Follow') {
            this.followed_dropdown.push({ name: this.disp_stock_name, abbriev: this.disp_stock });
            this.value = this.disp_stock;
            this.followButton = 'Unfollow';
          } else if (this.followButton === 'Unfollow') {
            this.followed_dropdown.splice(key, 1);
            this.followButton = 'Follow';
            this.value = '';
          }
        }).finally(() => {
          this.buttonDisabled = false;
        });
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
