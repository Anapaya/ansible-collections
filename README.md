# ansible-collections

The home for Ansible collections maintained by Anapaya.

## Requirements

Create a venv and install the requirements:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Testing

Run the sample playbook:

```bash
ansible-playbook playbook.yml -e appliance_address=APPLIANCE_API_ADDRESS
# for example:
ansible-playbook playbook.yml -e appliance_address=https://localhost
```

## Running the modules on a remote appliance

To run the module on a remote appliance, you need to install the pip requirements on the appliance first.
