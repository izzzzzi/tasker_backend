#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.orm import backref

from . import db
from .user import User


class Subscription(db.Model):
    __table_args__ = (
        db.PrimaryKeyConstraint("from_id", "to_id", name="uix_subscription"),
    )

    from_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    from_user = db.relationship(User, foreign_keys=[from_id], backref=backref("subscriptions_to", cascade="all,delete"))
    to_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    to_user = db.relationship(User, foreign_keys=[to_id], backref=backref("subscriptions_from", cascade="all,delete"))
    approved = db.Column(db.Boolean, nullable=False)
