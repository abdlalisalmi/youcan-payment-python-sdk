<p  align="center"><a  href="https://youcanpay.com"  target="_blank"><img  src="https://youcanpay.com/images/ycpay-logo.svg"  width="400"></a></p>
<!--
<p align="center">
<a href="https://youcanpay.com"><img src="https://github.com/NextmediaMa/youcan-payment-php-sdk/actions/workflows/tests.yml/badge.svg" alt="Tests"></a>
<a href="https://packagist.org/packages/youcanpay/payment-sdk"><img src="https://img.shields.io/packagist/dt/youcanpay/payment-sdk" alt="Total Downloads"></a>
<a href="https://packagist.org/packages/youcanpay/payment-sdk"><img src="https://img.shields.io/packagist/v/youcanpay/payment-sdk" alt="Latest Version"></a>
<a href="https://packagist.org/packages/youcanpay/payment-sdk"><img src="https://img.shields.io/packagist/l/youcanpay/payment-sdk" alt="License"></a>
</p>
-->
YouCan Pay is a payment platform initially developed to solve the payment gateway issue for e-merchants, And it's a simple way to accept timely payments online. You can use a Moroccan or international credit card to transfer money from a customer's bank account to yours.

This package allows the developers to interact easily with the [YouCan Pay API](https://youcanpay.com/docs).

## YouCan Pay SDK Setup

Instructions for adding the YouCan Pay SDK to your Python Applications.

#### Step 1: Requirements

- YouCan Pay Account.
- Your YouCan Pay `private_key` and `public_key` available in Settings > API Keys.
- This package installed in your Development / Production environment.

#### Step 2: Install YouCan Pay SDK

Open your Python project, add the following.

```bash
Coming Soon...
```

#### Step 3: Integrate YouCan Pay SDK with your project

In this documentaion I used Django as Python project envirement.

##### Step 3.1: Importing the package and working with some of it's method's

```python
from youcanpay import YouCanPay

# Initialize the SDK instance
youcanpay =  YouCanPay(private_key='pri_**', public_key='pub_**', sandbox_mode=True)
# Check the keys if is valid or not.
youcanpay.keys.check()
```

<!---
##### Step 2.1: YouCan Pay: Default Integration
If you choose to use JS integration, you must have an SSL certificate to run in production mode.

2.1.1: Copy this JS script between  `<head>...</head>`
```javascript
<script src="https://pay.youcan.shop/js/ycpay.js"></script>
```
2.1.2: Choose where you want to display payment information (Full Name, Card Numbers, CCV...), must be placed between the `<body>...</body>` tags.
```javascript
<div id="payment-card"></div>
<button id="pay">Pay</button>
```
2.1.3: Add this code just before the end of the `...</body>` tag.
```javascript
<script type="text/javascript">
  // Create a YouCan Pay instance.
  const ycPay = new YCPay(
    // String public_key (required): Login to your account.
    // Go to Settings and open API Keys and copy your key.
    "public_key",
    // Optional options object
    {
      formContainer: "#payment-card",
      // Defines what language the form should be rendered in, supports EN, AR, FR.
      locale: "en",

      // Whether the integration should run in sandbox (test) mode or live mode.
      isSandbox: false,

      // A DOM selector representing which component errors should be injected into.
      // If you omit this option, you may alternatively handle errors by chaining a .catch()
      // On the pay method.
      errorContainer: "#error-container",
    }
  );

  // Select which gateways to render
  ycPay.renderAvailableGateways(["CashPlus", "CreditCard"]);

  // Alternatively, you may use gateway specific render methods if you only need one.
  ycPay.renderCreditCardForm();
</script>
```

-->
