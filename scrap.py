from bs4 import BeautifulSoup

# Load HTML (you can replace this with a file read or request)
html_content = """
<div class="row" bis_skin_checked="1">
                    <template x-for="wallet in filteredWallets" :key="wallet.filename">
                        <div class="col-12 col-md-6 col-lg-4">
                            <div class="hp-select-box-item">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;">
                                    <div style="padding: 6px;">
                                        <div style="display: flex; align-items: center; text-align: left;">
                                            <div style="flex: 0 0 25%; padding: 12px;">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">
                                                </span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </template><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/0_safepal.png" alt="Safepal">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Safepal</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/1_trust.png" alt="Trust">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Trust</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/2_metamask.png" alt="Metamask">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Metamask</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/3_coinbase.png" alt="Coinbase">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Coinbase</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/aktionariat.png" alt="Aktionariat">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Aktionariat</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/alice.png" alt="Alice">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Alice</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/alpha_wallet.png" alt="Alpha Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Alpha Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/anchor.png" alt="Anchor">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Anchor</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/arculus.png" alt="Arculus">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Arculus</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/argent.png" alt="Argent">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Argent</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/at.wallet.png" alt="At Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">At Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/atomic.png" alt="Atomic">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Atomic</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/authereum.png" alt="Authereum">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Authereum</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/bakkt.png" alt="Bakkt">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Bakkt</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/binance_smart_chain.png" alt="Binance Smart Chain">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Binance Smart Chain</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/bit_keep.png" alt="Bit Keep">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Bit Keep</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/bit_pay.png" alt="Bit Pay">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Bit Pay</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/blockchain.png" alt="Blockchain">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Blockchain</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/bridge_wallet.png" alt="Bridge Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Bridge Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/coin98.png" alt="Coin98">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Coin98</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/coinomi.png" alt="Coinomi">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Coinomi</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/cool_wallet_s.png" alt="Cool Wallet S">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Cool Wallet S</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/cosmostation.png" alt="Cosmostation">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Cosmostation</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/crypto.com_defi_wallet.png" alt="Crypto com DeFi Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Crypto com DeFi Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/cybavo_wallet.png" alt="Cybavo Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Cybavo Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/d_cent_biometric_wallet.png" alt="D Cent Biometric Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">D Cent Biometric Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/d_cent_wallet.png" alt="D Cent Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">D Cent Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/dok_wallet.png" alt="Dok Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Dok Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/easy_pocket.jpg" alt="Easy Pocket">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Easy Pocket</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/eidoo.png" alt="Eidoo">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Eidoo</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/ellipal.png" alt="Ellipal">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Ellipal</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/equal.jpg" alt="Equal">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Equal</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/exodus.jpeg" alt="Exodus">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Exodus</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/fetch.jpg" alt="Fetch">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Fetch</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/girin_wallet.png" alt="Girin Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Girin Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/gnosis_safe_multisig.png" alt="Gnosis Safe Multisig">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Gnosis Safe Multisig</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/graph_protocol.jpg" alt="Graph Protocol">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Graph Protocol</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/grid_plus.png" alt="Grid Plus">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Grid Plus</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/harmony.png" alt="Harmony">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Harmony</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/huobi_wallet.png" alt="Huobi Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Huobi Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/iconex.png" alt="Iconex">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Iconex</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/infinito.png" alt="Infinito">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Infinito</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/infinity_wallet.png" alt="Infinity Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Infinity Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/karda_chain.png" alt="Karda Chain">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Karda Chain</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/keplr.png" alt="Keplr">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Keplr</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/keyring_pro.png" alt="Keyring Pro">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Keyring Pro</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/ledger_flex.png" alt="Ledger Flex">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Ledger Flex</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/ledger_live.png" alt="Ledger Live">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Ledger Live</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/ledger_nano_s.png" alt="Ledger Nano S">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Ledger Nano S</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/ledger_nano_s_plus.png" alt="Ledger Nano S Plus">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Ledger Nano S Plus</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/ledger_nano_x.png" alt="Ledger Nano X">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Ledger Nano X</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/ledger_stax.png" alt="Ledger Stax">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Ledger Stax</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/lobstr.png" alt="Lobstr">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Lobstr</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/loopring_wallet.png" alt="Loopring Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Loopring Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/maiar.png" alt="Maiar">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Maiar</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/math_wallet.png" alt="Math Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Math Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/meet.one.jpg" alt="Meet One">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Meet One</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/midas_wallet.png" alt="Midas Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Midas Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/morix_wallet.png" alt="Morix Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Morix Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/mykey.png" alt="Mykey">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Mykey</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/nash.png" alt="Nash">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Nash</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/ngrave.png" alt="Ngrave">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Ngrave</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/onto.png" alt="Onto">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Onto</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/ownbit.png" alt="Ownbit">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Ownbit</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/peak_defi_wallet.png" alt="Peak DeFi Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Peak DeFi Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/phantom.png" alt="Phantom">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Phantom</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/pillar.png" alt="Pillar">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Pillar</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/qubic.png" alt="Qubic">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Qubic</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/rainbow.png" alt="Rainbow">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Rainbow</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/spark_point.png" alt="Spark Point">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Spark Point</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/spatium.png" alt="Spatium">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Spatium</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/tangem.png" alt="Tangem">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Tangem</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/token_pocket.png" alt="Token Pocket">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Token Pocket</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/tokenary.png" alt="Tokenary">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Tokenary</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/torus.png" alt="Torus">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Torus</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/trezor_model_t.png" alt="Trezor Model T">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Trezor Model T</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/trust_vault.png" alt="Trust Vault">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Trust Vault</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/unstoppable_wallet.png" alt="Unstoppable Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Unstoppable Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/via_wallet.png" alt="Via Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Via Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/vision.png" alt="Vision">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Vision</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/wallet_connect.png" alt="Wallet Connect">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Wallet Connect</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/wallet.io.png" alt="Wallet IO">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Wallet IO</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/walleth.png" alt="Walleth">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Walleth</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/wazirx.png" alt="Wazirx">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Wazirx</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/xaman.png" alt="Xaman">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Xaman</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/xdc_wallet.png" alt="Xdc Wallet">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Xdc Wallet</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div><div class="col-12 col-md-6 col-lg-4" bis_skin_checked="1">
                            <div class="hp-select-box-item" bis_skin_checked="1">
                                <div class="wallet-card" @click="showWalletInfo(wallet.display_name, wallet.filename, wallet.path)" style="cursor: pointer;" bis_skin_checked="1">
                                    <div style="padding: 6px;" bis_skin_checked="1">
                                        <div style="display: flex; align-items: center; text-align: left;" bis_skin_checked="1">
                                            <div style="flex: 0 0 25%; padding: 12px;" bis_skin_checked="1">
                                                <img :src="wallet.path" :alt="wallet.display_name" height="64" class="img-icons" style="width: 3rem; height: 3rem; margin-bottom: 7px; border-radius: 50%;" src="https://web3anchorchain.com/images/wallets/zel_core.png" alt="Zel Core">
                                            </div>
                                            <div style="flex: 1; display: flex; justify-content: flex-start; align-items: center;" bis_skin_checked="1">
                                                <span class="wallet-name" style="font-size: 15px; font-weight: 700; letter-spacing: 1.5px;" x-text="wallet.display_name">Zel Core</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                </div>
"""

soup = BeautifulSoup(html_content, "html.parser")

wallets = []

for card in soup.find_all("div", class_="wallet-card"):
    img = card.find("img")
    name_tag = card.find("span", class_="wallet-name")

    if img:
        name = (
            (name_tag.text.strip() if name_tag and name_tag.text.strip() else None)
            or img.get("alt")
            or "Unknown Wallet"
        )

        logo = img.get("src")  # ✅ use EXACT image URL from HTML

        wallets.append({
            "name": name,
            "link": "#",   # no real link in your HTML
            "logo": logo
        })

# 🔥 print as Python array
print("wallets = [")
for w in wallets:
    print(f'    {w},')
print("]")