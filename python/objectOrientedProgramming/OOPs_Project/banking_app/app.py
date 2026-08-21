import streamlit as st

from bank import Bank


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Banking System",
    page_icon="🏦",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🏦 My Banking System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Simple Banking Management Application</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("Banking Menu")

menu = st.sidebar.radio(
    "Select an operation",
    [
        "🏠 Home",
        "➕ Create Account",
        "💰 Deposit Money",
        "💸 Withdraw Money",
        "👤 Account Details",
        "✏️ Update Details",
        "🗑️ Delete Account"
    ]
)


# ==================================================
# HOME
# ==================================================

if menu == "🏠 Home":

    st.header("Welcome to My Banking System")

    st.write(
        """
        This application allows you to manage your bank account.

        You can:

        - Create a new account
        - Deposit money
        - Withdraw money
        - View account details
        - Update your information
        - Delete your account
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Accounts",
            len(Bank.data)
        )

    with col2:
        total_balance = sum(
            account["balance"]
            for account in Bank.data
        )

        st.metric(
            "Total Balance",
            f"₹{total_balance}"
        )

    with col3:
        st.metric(
            "Maximum Deposit",
            "₹10,000"
        )


# ==================================================
# CREATE ACCOUNT
# ==================================================

elif menu == "➕ Create Account":

    st.header("Create New Account")

    with st.form("create_account_form"):

        name = st.text_input("Full Name")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=18
        )

        email = st.text_input("Email")

        pin = st.text_input(
            "4 Digit PIN",
            type="password",
            max_chars=4
        )

        submit = st.form_submit_button(
            "Create Account"
        )

    if submit:

        if not name:
            st.error("Please enter your name.")

        elif not email:
            st.error("Please enter your email.")

        elif not pin.isdigit() or len(pin) != 4:
            st.error("PIN must contain exactly 4 digits.")

        else:

            success, result = Bank.create_account(
                name,
                age,
                email,
                int(pin)
            )

            if success:

                st.success(
                    "Account created successfully!"
                )

                st.info(
                    f"Your Account Number: **{result['accountNo.']}**"
                )

                st.write("### Account Details")

                st.write(
                    f"**Name:** {result['name']}"
                )

                st.write(
                    f"**Email:** {result['email']}"
                )

                st.write(
                    f"**Balance:** ₹{result['balance']}"
                )

                st.warning(
                    "Please save your account number."
                )

            else:
                st.error(result)


# ==================================================
# DEPOSIT
# ==================================================

elif menu == "💰 Deposit Money":

    st.header("Deposit Money")

    acc_num = st.text_input(
        "Account Number"
    )

    pin = st.text_input(
        "PIN",
        type="password",
        max_chars=4
    )

    amount = st.number_input(
        "Deposit Amount",
        min_value=1,
        max_value=10000,
        step=100
    )

    if st.button("Deposit Money"):

        if not acc_num:
            st.error("Enter your account number.")

        elif not pin.isdigit():
            st.error("Invalid PIN.")

        else:

            success, result = Bank.deposit_money(
                acc_num,
                int(pin),
                amount
            )

            if success:

                st.success(
                    "Money deposited successfully!"
                )

                st.metric(
                    "Current Balance",
                    f"₹{result}"
                )

            else:
                st.error(result)


# ==================================================
# WITHDRAW
# ==================================================

elif menu == "💸 Withdraw Money":

    st.header("Withdraw Money")

    acc_num = st.text_input(
        "Account Number"
    )

    pin = st.text_input(
        "PIN",
        type="password",
        max_chars=4
    )

    amount = st.number_input(
        "Withdrawal Amount",
        min_value=1,
        max_value=10000,
        step=100
    )

    if st.button("Withdraw Money"):

        if not acc_num:
            st.error("Enter your account number.")

        elif not pin.isdigit():
            st.error("Invalid PIN.")

        else:

            success, result = Bank.withdraw_money(
                acc_num,
                int(pin),
                amount
            )

            if success:

                st.success(
                    "Money withdrawn successfully!"
                )

                st.metric(
                    "Current Balance",
                    f"₹{result}"
                )

            else:
                st.error(result)


# ==================================================
# ACCOUNT DETAILS
# ==================================================

elif menu == "👤 Account Details":

    st.header("Account Details")

    acc_num = st.text_input(
        "Account Number"
    )

    pin = st.text_input(
        "PIN",
        type="password",
        max_chars=4
    )

    if st.button("View Details"):

        if not pin.isdigit():
            st.error("Invalid PIN.")

        else:

            account = Bank.get_details(
                acc_num,
                int(pin)
            )

            if account:

                st.success(
                    "Account verified successfully."
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        f"**Name:** {account['name']}"
                    )

                    st.write(
                        f"**Age:** {account['age']}"
                    )

                    st.write(
                        f"**Email:** {account['email']}"
                    )

                with col2:

                    st.write(
                        f"**Account Number:** "
                        f"{account['accountNo.']}"
                    )

                    st.write(
                        f"**Balance:** "
                        f"₹{account['balance']}"
                    )

            else:
                st.error(
                    "Invalid account number or PIN."
                )


# ==================================================
# UPDATE DETAILS
# ==================================================

elif menu == "✏️ Update Details":

    st.header("Update Account Details")

    acc_num = st.text_input(
        "Account Number"
    )

    pin = st.text_input(
        "Current PIN",
        type="password",
        max_chars=4
    )

    st.write(
        "Leave a field empty if you don't want to change it."
    )

    new_name = st.text_input(
        "New Name"
    )

    new_email = st.text_input(
        "New Email"
    )

    new_pin = st.text_input(
        "New PIN",
        type="password",
        max_chars=4
    )

    if st.button("Update Details"):

        if not pin.isdigit():
            st.error("Invalid current PIN.")

        else:

            success, message = Bank.update_details(
                acc_num,
                int(pin),
                new_name,
                new_email,
                new_pin
            )

            if success:
                st.success(message)

            else:
                st.error(message)


# ==================================================
# DELETE ACCOUNT
# ==================================================

elif menu == "🗑️ Delete Account":

    st.header("Delete Account")

    st.warning(
        "⚠️ This action cannot be undone."
    )

    acc_num = st.text_input(
        "Account Number"
    )

    pin = st.text_input(
        "PIN",
        type="password",
        max_chars=4
    )

    confirm = st.checkbox(
        "I understand that my account will be permanently deleted."
    )

    if st.button(
        "Delete Account",
        type="primary"
    ):

        if not confirm:

            st.error(
                "Please confirm account deletion."
            )

        elif not pin.isdigit():

            st.error(
                "Invalid PIN."
            )

        else:

            success, message = Bank.delete_account(
                acc_num,
                int(pin)
            )

            if success:

                st.success(message)

                st.balloons()

            else:

                st.error(message)