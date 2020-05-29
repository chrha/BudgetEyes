<template>
  <div> 
    <v-container fluid> 
      <v-row>
        <v-col>
          <h2> Your followed Stocks: </h2>
          <v-select 
          v-model="chosenStock"
          prepend-inner-icon='mdi-chart-line'
          :items="getStockNames"
          outlined
          @change="getStockData"
          > </v-select>
          <v-container v-show="chosenStock" class="mx-auto">
            <stockGraph :stockName="stockAbbriev" :stockData="stockData"/> 
          </v-container>

        </v-col>
          <v-col>
            <v-card v-show="!editMode" max-width="700" color="#B39DDB">
              <v-avatar size="300">
                <v-img class="white--text align-end md-3" heigth="200px"
                :src="imgsrc">
                </v-img>
              </v-avatar>
              <v-card-actions>
                <br/>
                <v-btn text color="dark" small tile @click="toggleEditMode"> 
                  Edit profile  <v-icon >mdi-pencil</v-icon> 
                </v-btn>
                 <v-spacer></v-spacer>
                 <input type="file" ref="file" style="display:none" @change="fileChanged($event)"> 
                <v-btn text color="dark" small tile @click="$refs.file.click()">
                  <v-icon> mdi-image-plus </v-icon> Change picture
                </v-btn>
              </v-card-actions>
              <v-card-subtitle class="text-center subtitle-1"> 
                {{ this.$store.state.username }} 
              </v-card-subtitle>
              <v-list-item v-for="(item, key, index) in profile" :key="index">
               <v-card-text class="text-left"> {{keys[index]}} </v-card-text>
               <v-card-text class="text-center">
                 {{item}} 
                </v-card-text>
              </v-list-item>
              <v-list-item>
                <v-card-text class="text-center"> Bio </v-card-text>
              </v-list-item>
              <v-list-item> 
                <v-card-text class="text-center">
                  {{bio}} 
                </v-card-text>
              </v-list-item>
            </v-card>
            <v-form v-show="editMode"
            ref="form"
            >
              <v-text-field
              v-model="profile.name"
              label="Name"
              >
              {{profile.name}}
              </v-text-field>
              <v-text-field
              v-model="profile.birthDate"
              label="Birth date"
              >
              {{profile.birthDate}}
              </v-text-field>
              <v-text-field
              v-model="profile.city"
              label="City"
              >
              {{profile.city}}
              </v-text-field>
              <v-text-field
              v-model="profile.email"
              label="Email"
              >
              {{profile.email}}
              </v-text-field>                                                
              <v-text-field
              v-model="profile.dateJoined"
              label="Member since"
              >
              {{profile.dateJoined}}
              </v-text-field>
              <v-textarea
              v-model="bio"
              label="Biography"
              >
              {{bio}}
              </v-textarea>
              <v-btn  @click="saveChanges"> Save changes </v-btn>
            </v-form>
          </v-col>
        <v-col>
        <h2>Active Forums Posts</h2>
        <h4> To be implemented </h4>
        </v-col>

      </v-row>
    </v-container>  
  </div>
</template>

<script>

import axiosInstance from '../ajax/client';
import stockGraph from '../stocks/StockGraph.vue';

export default {
  name: 'Profile',
  components: {
    stockGraph,
  },
  data() {
    return {
      profile: {
        name: '',
        birthDate: '',
        city: '',
        email: '',
        dateJoined: '',
      },
      bio: '',
      followedStocks: [],
      imgsrc: '',
      editMode: false,
      chosenStock: '',
      stockAbbriev: '',
      keys: ['Name', 'Birth Date', 'City', 'Email', 'Member since'],
      rules: [
        (value) => !value || value.size < 2000000 || 'Avatar size should be less than 2 MB!',
      ],
      stockData: {},
    };
  },
  computed: {
    getStockNames() {
      const arr = [];
      for (let i = 0; i < this.followedStocks.length; i += 1) {
        arr.push(this.followedStocks[i].name);
      }
      return arr;
    },
  },
  methods: {
    toggleEditMode() {
      this.editMode = !this.editMode;
    },
    saveChanges() {
      const data = {
        birth_date: this.profile.birthDate,
        bio: this.bio,
        city: this.profile.city,
        email: this.profile.email,
        first_name: this.profile.name.split(' ')[0],
        last_name: this.profile.name.split(' ')[1],
        username: this.$store.state.username,
      };
      axiosInstance.put('auth/profile/', data, { headers: { Authorization: `Token ${this.$cookies.get('token')}` } });
      this.toggleEditMode();
    },
    fileChanged(event) {
      const file = event.target.files[0];
      this.imgsrc = URL.createObjectURL(file);
      const formData = new FormData();
      formData.append('profilepic', file);
      axiosInstance.put('auth/profilepic/', formData, 
        { headers: { Authorization: `Token ${this.$cookies.get('token')}` } });
    },
    hexToBase64(str) {
      return btoa(String.fromCharCode.apply(null, str.replace(/\r|\n/g, '').replace(/([\da-fA-F]{2}) ?/g, '0x$1 ').replace(/ +$/, '').split(' ')));
    },
    getStockData() {
      const stock = this.followedStocks.find((elem) => elem.name === this.chosenStock).abbriev;
      this.stockAbbriev = stock;
      axiosInstance.put('stocks/query/', { stocks: [stock] })
        .then((response) => {
          this.stockData = response.data[stock];
        }).catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    axiosInstance.get('auth/profile/', { headers: { Authorization: `Token ${this.$cookies.get('token')}` } })
      .then((response) => {
        this.profile.birthDate = response.data.birth_date;
        this.bio = response.data.bio;
        this.profile.name = `${response.data.userinfo.first_name} ${response.data.userinfo.last_name}`;
        this.profile.city = response.data.city;
        this.profile.email = response.data.userinfo.email;
        this.profile.dateJoined = response.data.userinfo.date_joined;
        this.followedStocks = response.data.stocks;
        this.imgsrc = 'https://f0.pngfuel.com/png/340/956/profile-user-icon-png-clip-art.png';
      }).catch((error) => {
      // eslint-disable-next-line
      console.log(error);
      });
    /*
    axiosInstance.get('auth/profilepic/', 
    { headers: { Authorization: `Token ${this.$store.state.token}` } })
      .then((response) => {
        console.log(response.data);
        // this.imgsrc = `data:image/jpeg;base64,${data}`;
        const reader = new FileReader();
        reader.readAsBinaryString(response.data);
        reader.onloadend = function () {
          this.imgsrc = reader.result;
        }; 
      });
      */
  },
};


</script>

<style scoped>
span.key {
  text-align: left;
  float: left;
}

span .value {
  text-align: center;
}
</style>

