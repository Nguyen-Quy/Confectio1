<template>
	<div class="CheckOut">
		<div class="container column is-12">
			<h1 class="text-uppercase font-weight-normal">Checkout</h1>
		</div>
		<div class="row mainRow">
			<!--Card 1-->
			<div class="col-sm-8">
				<div class="card card-cascade wider shadow p-3 mb-5">
					<h2 class="subtitle">Shipping details</h2>

					<p class="has-text-grey mb-4">* All fields are required</p>
					<div class="row from_checkout form-group">
						<div class="column1 is-6">
							<div class="field">
								<label>First name*</label>
								<div class="control">
									<input type="text" class="input" v-model="first_name" />
								</div>
							</div>

							<div class="field">
								<label>Last name*</label>
								<div class="control">
									<input type="text" class="input" v-model="last_name" />
								</div>
							</div>

							<div class="field">
								<label>E-mail*</label>
								<div class="control">
									<input type="email" class="input" v-model="email" />
								</div>
							</div>

							<div class="field">
								<label>Phone*</label>
								<div class="control">
									<input type="text" class="input" v-model="phone" />
								</div>
							</div>
						</div>

						<div class="column2 is-6">
							<div class="field">
								<label>Address*</label>
								<div class="control">
									<input type="text" class="input" v-model="address" />
								</div>
							</div>

							<div class="field">
								<label>Zip code*</label>
								<div class="control">
									<input type="text" class="input" v-model="zipcode" />
								</div>
							</div>

							<div class="field">
								<label>Place*</label>
								<div class="control">
									<input type="text" class="input" v-model="place" />
								</div>
							</div>
						</div>
					</div>
					<div class="notification is-danger mt-4" v-if="errors.length">
						<p style="color: red" v-for="error in errors" :key="error">
							{{ error }}
						</p>
					</div>
				</div>
			</div>

			<!--Card 2-->
			<div class="col-sm-4">
				<div class="card card-cascade card-ecommerce wider shadow p-3 mb-5">
					<!--Card Body-->
					<div class="card-body card-body-cascade">
						<!--Card Description-->
						<div>
							<p class="quantity">
								Quantity
								<span class="float-right text1">{{ cartTotalLength }}</span>
							</p>
							<p class="subtotal">
								Subtotal<span class="float-right text1"
									>{{
										cartTotalPrice
											.toString()
											.replace(/\B(?=(\d{3})+(?!\d))/g, ".")
									}}
									VNĐ</span
								>
							</p>
							<p class="shipping">
								Shipping<span class="float-right text1"
									>{{
										(cartTotalPrice * 0.1)
											.toString()
											.replace(/\B(?=(\d{3})+(?!\d))/g, ".")
									}}
									VNĐ</span
								>
							</p>
							<p class="total">
								<strong>Total</strong
								><span class="float-right totalText1"
									><span class="totalText2"
										>{{
											(cartTotalPrice + cartTotalPrice * 0.1)
												.toString()
												.replace(/\B(?=(\d{3})+(?!\d))/g, ".")
										}}
										VNĐ</span
									></span
								>
							</p>
						</div>

						<div class="payment mb-5" id="card-element"></div>

						<!--Card footer-->
						<div class="purchaseLink" v-if="cartTotalLength">
							<button class="card-footer text-center" @click="submitForm">
								PURCHASE
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";

export default {
	name: "Checkout",
	data() {
		return {
			cart: {
				items: [],
			},
			stripe: {},
			card: {},
			first_name: "",
			last_name: "",
			email: "",
			phone: "",
			address: "",
			zipcode: "",
			place: "",
			errors: [],
		};
	},
	mounted() {
		document.title = "Checkout | BK";

		this.cart = this.$store.state.cart;

		if (this.cartTotalLength > 0) {
			this.stripe = Stripe(
				"pk_test_51M7WBDB4eGNJFQglQXVVmjvMHzMeZgtyH3N7iycdQkoJfEvI1f3dZhk8qwN8jBkyyd1cK15tWNJFA3sIBphG03NT00knSIYmK8"
			);
			const elements = this.stripe.elements();
			this.card = elements.create("card", { hidePostalCode: true });

			this.card.mount("#card-element");
		}
	},
	methods: {
		getItemTotal(item) {
			return item.quantity * item.product.price;
		},
		submitForm() {
			this.errors = [];

			if (this.first_name === "") {
				this.errors.push("The first name field is missing!");
			}

			if (this.last_name === "") {
				this.errors.push("The last name field is missing!");
			}

			if (this.email === "") {
				this.errors.push("The email field is missing!");
			}

			if (this.phone === "") {
				this.errors.push("The phone field is missing!");
			}

			if (this.address === "") {
				this.errors.push("The address field is missing!");
			}

			if (this.zipcode === "") {
				this.errors.push("The zip code field is missing!");
			}

			if (this.place === "") {
				this.errors.push("The place field is missing!");
			}

			if (!this.errors.length) {
				this.$store.commit("setIsLoading", true);

				this.stripe.createToken(this.card).then(result => {
					if (result.error) {
						this.$store.commit("setIsLoading", false);

						this.errors.push(
							"Something went wrong with Stripe. Please try again"
						);

						console.log(result.error.message);
					} else {
						this.stripeTokenHandler(result.token);
					}
				});
			}
		},
		async stripeTokenHandler(token) {
			const items = [];

			for (let i = 0; i < this.cart.items.length; i++) {
				const item = this.cart.items[i];
				const obj = {
					product: item.product.id,
					quantity: item.quantity,
					price: item.product.price * item.quantity,
				};

				items.push(obj);
			}

			const data = {
				first_name: this.first_name,
				last_name: this.last_name,
				email: this.email,
				address: this.address,
				zipcode: this.zipcode,
				place: this.place,
				phone: this.phone,
				items: items,
				stripe_token: token.id,
			};

			await axios
				.post("/api/v1/checkout/", data)
				.then(response => {
					this.$store.commit("clearCart");
					this.$router.push("/cart/success");
				})
				.catch(error => {
					this.errors.push("Something went wrong. Please try again");

					console.log(error);
				});

			this.$store.commit("setIsLoading", false);
		},
	},
	computed: {
		cartTotalPrice() {
			return this.cart.items.reduce((acc, curVal) => {
				return (acc += curVal.product.price * curVal.quantity);
			}, 0);
		},
		cartTotalLength() {
			return this.cart.items.reduce((acc, curVal) => {
				return (acc += curVal.quantity);
			}, 0);
		},
	},
};
</script>
