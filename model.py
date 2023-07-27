import os, torch, torch.nn as nn, torch.utils.data as data, torchvision as tv
import lightning as L
import datetime as dt

encoder = nn.Sequential(
    nn.Linear(1500, 300), nn.ReLU(), nn.Linear(300, 30), nn.ReLU(), nn.Linear(30, 5)
)
decoder = nn.Sequential(
    nn.Linear(5, 30), nn.ReLU(), nn.Linear(30, 300), nn.ReLU(), nn.Linear(300, 1500)
)

tickers = [
    "AXP",
    "AMGN",
    "AAPL",
    "BA",
    "CAT",
    "CSCO",
    "CVX",
    "GS",
    "HD",
    "HON",
    "IBM",
    "INTC",
    "JNJ",
    "KO",
    "JPM",
    "MCD",
    "MMM",
    "MRK",
    "MSFT",
    "NKE",
    "PG",
    "TRV",
    "UNH",
    "CRM",
    "VZ",
    "V",
    "WBA",
    "WMT",
    "DIS",
    "DOW",
]
companies = [
    "American Express Co",
    "Amgen Inc",
    "Apple Inc",
    "Boeing Co",
    "Caterpillar Inc",
    "Cisco Systems Inc",
    "Chevron Corp",
    "Goldman Sachs Group Inc",
    "Home Depot Inc",
    "Honeywell International Inc",
    "International Business Machines Corp",
    "Intel Corp",
    "Johnson & Johnson",
    "Coca-Cola Co",
    "JPMorgan Chase & Co",
    "McDonald`s Corp",
    "3M Co",
    "Merck & Co Inc",
    "Microsoft Corp",
    "Nike Inc",
    "Procter & Gamble Co",
    "Travelers Companies Inc",
    "UnitedHealth Group Inc",
    "Salesforce Inc",
    "Verizon Communications Inc",
    "Visa Inc",
    "Walgreens Boots Alliance Inc",
    "Walmart Inc",
    "Walt Disney Co",
    "Dow Inc",
]

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()


class DeepAutoEncoder(L.LightningModule):
    def __init__(self, encoder, decoder):
        super().__init__()
        self.encoder, self.decoder = encoder, decoder

    def training_step(self, batch, batch_idx):
        x, y = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = nn.functional.mse_loss(x_hat, x)
        self.log("train_loss", loss)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=1e-3)
